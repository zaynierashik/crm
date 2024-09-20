import io

from django.shortcuts import render, redirect, get_object_or_404
from django.http import *
from django.utils.timezone import now
from datetime import datetime
from django.urls import reverse
from django.db.models import Sum
from .models import *
from .services import predict_revenue_for_company
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout, update_session_auth_hash
from openpyxl import Workbook # type: ignore
from openpyxl.styles import Alignment, Font, Border, Side # type: ignore

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def login(request):
    if 'staff_id' in request.session:
        return redirect('dashboard')
    
    if request.method == 'POST':
        return login_authentication(request)
    
    return render(request, 'login.html')

# Login Authentication
def login_authentication(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Staff.objects.get(email=email)
        except Staff.DoesNotExist:
            error_message = "Invalid email or password!"
            return HttpResponseRedirect(reverse('login') + f'?error_message={error_message}')

        if not check_password(password, user.password):
            error_message = "Invalid email or password!"
            return HttpResponseRedirect(reverse('login') + f'?error_message={error_message}')

        if not user.status:
            error_message = "Your account is inactive. Please contact support."
            return HttpResponseRedirect(reverse('login') + f'?error_message={error_message}')

        request.session['staff_id'] = user.id
        request.session['staff_email'] = user.email
        request.session['staff_full_name'] = user.full_name

        request.session.set_expiry(7200)
        return redirect('dashboard')

    return render(request, 'login.html')

def user(request):
    if 'user_id' in request.session:
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        return user_authentication(request)
    
    return render(request, 'userauthentication.html')

# User Registration
def add_newuser(request):
    if request.method == 'POST':
        full_name = request.POST.get('user-name')
        email = request.POST.get('email-address')
        password = request.POST.get('password')
        
        if not full_name or not email or not password:
            error_message = "All fields are required!"
            return HttpResponseRedirect(reverse('user') + f'?error_message={error_message}')

        if User.objects.filter(email=email).exists():
            error_message = "Email is already in use!"
            return HttpResponseRedirect(reverse('user') + f'?error_message={error_message}')

        try:
            new_user = User(full_name=full_name, email=email, password=make_password(password))
            new_user.save()
            messages.success(request, "Account created successfully.")
            return redirect('user')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('user')

    return render(request, 'signup.html')

# User Login Authentication
def user_authentication(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error_message = "Invalid email or password!"
            return HttpResponseRedirect(reverse('user') + f'?error_message={error_message}')

        if not check_password(password, user.password):
            error_message = "Invalid email or password!"
            return HttpResponseRedirect(reverse('user') + f'?error_message={error_message}')

        if not user.status:
            error_message = "Your account is inactive. Please contact support."
            return HttpResponseRedirect(reverse('user') + f'?error_message={error_message}')

        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        request.session['user_full_name'] = user.full_name

        request.session.set_expiry(7200)
        return redirect('user_dashboard')

    return redirect('user')

def profile(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    return render(request, 'profile.html', {'user': user})

def setting(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    return render(request, 'setting.html', {'user': user})

def logout(request):
    request.session.flush()
    return redirect('login')

def dashboard(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)
    
    companies = Company.objects.order_by('company_name')
    contacts = Contact.objects.select_related('company').all()
    sectors = Sector.objects.values('id', 'sector_name').order_by('sector_name')
    services = Service.objects.values('id', 'service_name').distinct().order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').distinct().order_by('brand_name')
    products = Product.objects.values('id', 'product_name').distinct().order_by('product_name')
    partners = Partner.objects.values('id', 'partner_name').order_by('partner_name')
    cities = Company.objects.values_list('city', flat=True).distinct().order_by('city')
    staffs = Staff.objects.all()

    company_count = Company.objects.count()

    total_revenue = Requirement.objects.filter(status='Completed').aggregate(total_revenue=Sum('price'))['total_revenue'] or 0.00

    city_filter = request.GET.get('city', None)
    status_filter = request.GET.get('status', 'active')

    if city_filter:
        companies = companies.filter(city=city_filter)

    if status_filter:
        status_value = status_filter.lower() == 'active'
        companies = companies.filter(status=status_value)

    paginator = Paginator(companies, 15)
    page = request.GET.get('page')

    try:
        companies_page = paginator.page(page)
    except PageNotAnInteger:
        companies_page = paginator.page(1)
    except EmptyPage:
        companies_page = paginator.page(paginator.num_pages)

    company_id = Company.objects.first().id
    predicted_revenue = predict_revenue_for_company(company_id)

    context = {'companies': companies, 'contacts': contacts, 'sectors': sectors, 'services': services, 'brands': brands, 'products': products, 
               'partners': partners, 'cities': cities, 'staffs': staffs, 'total_revenue': total_revenue, 'company_count': company_count, 'companies': companies_page, 'paginator': paginator, 'page_obj': companies_page, 'user': user,'predicted_revenue': predicted_revenue[0]}

    return render(request, 'index.html', context)

def user_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('user')
    
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    company_added = request.GET.get('company_added', False)
    company = Company.objects.filter(created_by=user)
    context = {'company_added': company_added, 'company': company, 'user': user}

    return render(request, 'userdashboard.html', context)

def company(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    companies = Company.objects.order_by('company_name')
    contacts = Contact.objects.select_related('company').all()
    sectors = Sector.objects.values('id', 'sector_name').order_by('sector_name')
    services = Service.objects.values('id', 'service_name').distinct().order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').distinct().order_by('brand_name')
    products = Product.objects.values('id', 'product_name').distinct().order_by('product_name')
    partners = Partner.objects.values('id', 'partner_name').order_by('partner_name')
    cities = Company.objects.values_list('city', flat=True).distinct().order_by('city')
    staffs = Staff.objects.all()

    active_companies = Company.objects.filter(status=True).order_by('company_name')
    inactive_companies = Company.objects.filter(status=False).order_by('company_name')

    company_count = Company.objects.count()
    initiated_count = Requirement.objects.filter(status="Initiated").count()
    pipeline_count = Requirement.objects.filter(status="Pipeline").count()
    completed_count = Requirement.objects.filter(status="Completed").count()

    city_filter = request.GET.get('city', None)
    status_filter = request.GET.get('status', 'active')

    if city_filter:
        active_companies = active_companies.filter(city=city_filter)
        inactive_companies = inactive_companies.filter(city=city_filter)

    if status_filter:
        status_value = status_filter.lower() == 'active'
        if status_value:
            active_companies = active_companies.filter(status=True)
        else:
            inactive_companies = inactive_companies.filter(status=False)

    paginator_active = Paginator(active_companies, 10)
    page_active = request.GET.get('page_active')

    try:
        active_companies_page = paginator_active.page(page_active)
    except PageNotAnInteger:
        active_companies_page = paginator_active.page(1)
    except EmptyPage:
        active_companies_page = paginator_active.page(paginator_active.num_pages)

    paginator_inactive = Paginator(inactive_companies, 10)
    page_inactive = request.GET.get('page_inactive')

    try:
        inactive_companies_page = paginator_inactive.page(page_inactive)
    except PageNotAnInteger:
        inactive_companies_page = paginator_inactive.page(1)
    except EmptyPage:
        inactive_companies_page = paginator_inactive.page(paginator_inactive.num_pages)

    context = {'companies': companies, 'contacts': contacts, 'sectors': sectors, 'services': services, 'brands': brands, 'products': products, 'partners': partners, 'cities': cities, 'staffs': staffs, 'company_count': company_count,
                'initiated_count': initiated_count, 'pipeline_count': pipeline_count, 'completed_count': completed_count, 'active_companies': active_companies_page, 'inactive_companies': inactive_companies_page,
                'paginator_active': paginator_active, 'paginator_inactive': paginator_inactive, 'page_active': page_active, 'page_inactive': page_inactive, 'user': user}

    return render(request, 'company.html', context)

def add_newcompany(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    if request.method == 'POST':
        company_name = request.POST.get('company-name')

        if Company.objects.filter(company_name=company_name).exists():
            error_message = "Company with this name already exists!"
            return HttpResponseRedirect(reverse('company') + f'?add-company&error_message={error_message}&company_name={company_name}')

        sector_id = request.POST.get('sector')
        if sector_id:
            try:
                sector_id = int(sector_id)
                sector = Sector.objects.get(id=sector_id)
            except (ValueError, Sector.DoesNotExist):
                sector = None
        else:
            sector = None
        
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        via = request.POST.get('via')
        website = request.POST.get('website')
        
        if via == 'Referral':
            referral = request.POST.get('referral')
            partner_name = None
        elif via == 'Partner':
            partner_id = request.POST.get('partner')
            partner_name = Partner.objects.filter(id=partner_id).first()
            if partner_name:
                partner = partner_name
                referral = None
        else:
            referral = None
            partner = None

        company = Company(company_name=company_name, sector=sector, address=address, city=city, state=state, country=country, via=via, referral_name=referral, partner_name=partner, website=website, created_by=user)
        company.save()

        contact_names = request.POST.getlist('contact-name[]')
        designations = request.POST.getlist('designation[]')
        emails = request.POST.getlist('email-address[]')
        contact_numbers = request.POST.getlist('contact-number[]')
        dobs = request.POST.getlist('date[]')
        religions = request.POST.getlist('religion[]')

        for i in range(len(contact_names)):
            if contact_names[i]:
                dob = dobs[i] if dobs[i] else None
                contact_person = Contact(company=company, contact_name=contact_names[i], designation=designations[i], email=emails[i], phone_number=contact_numbers[i], dob=dob, religion=religions[i])
                contact_person.save()
                
        return redirect(reverse('company'))
    else:
        return HttpResponse("Form Submission Error!")

def company_profile(request):
    if 'user_id' not in request.session:
        return redirect('user')

    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    sectors = Sector.objects.values('id', 'sector_name').order_by('sector_name')
    partners = Partner.objects.values('id', 'partner_name').order_by('partner_name')
    user_company = Company.objects.filter(created_by=user).first()

    if user_company:
        contacts = Contact.objects.filter(company=user_company)
        return render(request, 'companyprofile.html', {'user': user, 'company': user_company, 'contacts': contacts, 'sectors': sectors, 'partners': partners, 'edit_mode': True})
    else:
        return render(request, 'companyprofile.html', {'user': user, 'sectors': sectors, 'partners': partners, 'edit_mode': False})
    
def contract(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)
    
    requirements = Requirement.objects.select_related('company').all().order_by('-date')
    services = Service.objects.values('id', 'service_name').order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').order_by('brand_name')
    products = Product.objects.values('id', 'product_name').order_by('product_name')

    total_request = Request.objects.count()
    total_requirement = Requirement.objects.count()
    pipeline_count = Requirement.objects.filter(progress="Pipeline").count()
    completed_count = Requirement.objects.filter(progress="Completed").count()

    paginator = Paginator(requirements, 10)
    page = request.GET.get('requirements_page')

    try:
        requirements_page = paginator.page(page)
    except PageNotAnInteger:
        requirements_page = paginator.page(1)
    except EmptyPage:
        requirements_page = paginator.page(paginator.num_pages)

    context = {'user': user, 'requirements': requirements, 'services': services, 'brands': brands, 'products': products, 'total_request': total_request, 'total_requirement': total_requirement, 
               'pipeline_count': pipeline_count, 'completed_count': completed_count, 'requirement_count': requirements.count(), 'requirements_page': requirements_page, 'paginator': paginator}
    
    return render(request, 'contract.html', context)

def requirement(request):
    if 'user_id' not in request.session:
        return redirect('user')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id=user_id)

    company = Company.objects.filter(created_by=user).first()

    services = Service.objects.values('id', 'service_name').distinct().order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').distinct().order_by('brand_name')
    products = Product.objects.values('id', 'product_name').distinct().order_by('product_name')
    requests = Request.objects.filter(company=company).order_by('-date')
    requirements = Requirement.objects.filter(company=company).order_by('-date')

    total_request = Request.objects.count()
    total_requirement = Requirement.objects.count()
    pipeline_count = Requirement.objects.filter(progress="Pipeline").count()
    completed_count = Requirement.objects.filter(progress="Completed").count()

    paginator = Paginator(requirements, 10)
    page = request.GET.get('requirements_page')

    try:
        requirements_page = paginator.page(page)
    except PageNotAnInteger:
        requirements_page = paginator.page(1)
    except EmptyPage:
        requirements_page = paginator.page(paginator.num_pages)

    context = {'services': services, 'brands': brands, 'products': products, 'requests': requests, 'requirements': requirements, 'user': user, 'total_request': total_request, 'total_requirement': total_requirement, 
               'pipeline_count': pipeline_count, 'completed_count': completed_count, 'requirement_count': requirements.count(), 'requirements_page': requirements_page, 'paginator': paginator}

    return render(request, 'requirement.html', context)

def contact(request):
    if 'user_id' not in request.session:
        return redirect('user')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id=user_id)

    company = Company.objects.filter(created_by=user).first()
    contacts = Contact.objects.filter(company=company).order_by('contact_name')

    paginator = Paginator(contacts, 10)
    page = request.GET.get('contacts_page')

    try:
        contacts_page = paginator.page(page)
    except PageNotAnInteger:
        contacts_page = paginator.page(1)
    except EmptyPage:
        contacts_page = paginator.page(paginator.num_pages)

    context = {'user': user, 'company': company, 'contacts': contacts, 'contact_count': contacts.count(), 'contacts_page': contacts_page, 'paginator': paginator}
    return render(request, 'contact.html', context)

def add_newcontact(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    company = Company.objects.filter(created_by=user).first()

    if request.method == "POST":
        contact_name = request.POST.get('contact-name')
        designation = request.POST.get('designation')
        email = request.POST.get('email-address')
        contact_number = request.POST.get('contact-number')
        dob = request.POST.get('date')
        religion = request.POST.get('religion')

        if dob:
            try:
                dob = datetime.strptime(dob, '%Y-%m-%d').date()
            except ValueError:
                dob = None
        else:
            dob = None

        contact = Contact(company=company, contact_name=contact_name, designation=designation, email=email, phone_number=contact_number, DOB=dob, religion=religion)
        contact.save()
        return redirect(reverse('contact'))
    
    return render(request, 'contact.html', {'user': user, 'company': company})

@require_POST
def update_contact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact-id')
        contact_obj = get_object_or_404(Contact, id=contact_id)

        contact_obj.contact_name = request.POST.get('contact-name')
        contact_obj.designation = request.POST.get('designation')
        contact_obj.email = request.POST.get('email-address')
        contact_obj.phone_number = request.POST.get('contact-number')
        # contact_obj.DOB = request.POST.get('date')

        # dob = request.POST.get('date')
        # if dob:
        #     contact_obj.DOB = dob
        # else:
        #     contact_obj.DOB = None
            
        # contact_obj.religion = request.POST.get('religion')
        contact_obj.save()
        messages.success(request, "Contact updated successfully.")
        
        return redirect('contact')

    return redirect('contact')

def partner(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    partners = Partner.objects.order_by('partner_name')
    partner_count = Partner.objects.count()
    paginator = Paginator(partners, 10)
    page = request.GET.get('page')

    try:
        partners_page = paginator.page(page)
    except PageNotAnInteger:
        partners_page = paginator.page(1)
    except EmptyPage:
        partners_page = paginator.page(paginator.num_pages)

    context = {'partners': partners, 'partner_count': partner_count, 'partners': partners_page, 'paginator': paginator, 'page_obj': partners_page, 'user': user}

    return render(request, 'partner.html', context)

def staff(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    staffs = Staff.objects.order_by('full_name')
    employee_count = Staff.objects.count()
    admin_count = Staff.objects.filter(role="Admin").count()
    staff_count = Staff.objects.filter(role="Staff").count()
    inactive_count = Staff.objects.filter(status=False).count()
    paginator = Paginator(staffs, 10)
    page = request.GET.get('page')

    try:
        staffs_page = paginator.page(page)
    except PageNotAnInteger:
        staffs_page = paginator.page(1)
    except EmptyPage:
        staffs_page = paginator.page(paginator.num_pages)

    context = {'staffs': staffs, 'employee_count': employee_count, 'admin_count': admin_count, 'staff_count': staff_count, 'inactive_count': inactive_count, 'staffs': staffs_page, 'paginator': paginator, 'page_obj': staffs_page, 'user': user}

    return render(request, 'staff.html', context)

def transaction(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    companies = Company.objects.order_by('company_name')
    contacts = Contact.objects.select_related('company').all()
    sectors = Sector.objects.values('id', 'sector_name').order_by('sector_name')
    services = Service.objects.values('id', 'service_name').distinct().order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').distinct().order_by('brand_name')
    products = Product.objects.values('id', 'product_name').distinct().order_by('product_name')
    partners = Partner.objects.values('id', 'partner_name').order_by('partner_name')
    cities = Company.objects.values_list('city', flat=True).distinct().order_by('city')
    staffs = Staff.objects.all()

    context = {'companies': companies, 'contacts': contacts, 'sectors': sectors, 'services': services, 'brands': brands, 'products': products, 
               'partners': partners, 'cities': cities, 'staffs': staffs, 'user': user}

    return render(request, 'transaction.html', context)

def sector(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    sectors = Sector.objects.order_by('sector_name')
    sector_count = Sector.objects.count()
    paginator = Paginator(sectors, 10)
    page = request.GET.get('page')

    try:
        sectors_page = paginator.page(page)
    except PageNotAnInteger:
        sectors_page = paginator.page(1)
    except EmptyPage:
        sectors_page = paginator.page(paginator.num_pages)

    context = {'sectors': sectors, 'sector_count': sector_count, 'sectors': sectors_page, 'paginator': paginator, 'page_obj': sectors_page, 'user': user}

    return render(request, 'sector.html', context)

def service(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    services = Service.objects.order_by('service_name')
    service_count = Service.objects.count()
    paginator = Paginator(services, 10)
    page = request.GET.get('page')

    try:
        services_page = paginator.page(page)
    except PageNotAnInteger:
        services_page = paginator.page(1)
    except EmptyPage:
        services_page = paginator.page(paginator.num_pages)

    context = {'services': services, 'service_count': service_count, 'services': services_page, 'paginator': paginator, 'page_obj': services_page, 'user': user}

    return render(request, 'service.html', context)

def brand(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    brands = Brand.objects.order_by('brand_name')
    brand_count = Brand.objects.count()
    paginator = Paginator(brands, 10)
    page = request.GET.get('page')

    try:
        brand_page = paginator.page(page)
    except PageNotAnInteger:
        brand_page = paginator.page(1)
    except EmptyPage:
        brand_page = paginator.page(paginator.num_pages)

    context = {'brands': brands, 'brand_count': brand_count, 'brands': brand_page, 'paginator': paginator, 'page_obj': brand_page, 'user': user}

    return render(request, 'brand.html', context)

# New Company Profile Submission
def add_companyprofile(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        company_name = request.POST.get('company-name')

        if Company.objects.filter(company_name=company_name).exists():
            error_message = "Company with this name already exists!"
            return HttpResponseRedirect(reverse('company_profile') + f'?add-company&error_message={error_message}&company_name={company_name}')

        sector_id = request.POST.get('sector')
        if sector_id:
            try:
                sector_id = int(sector_id)
                sector = Sector.objects.get(id=sector_id)
            except (ValueError, Sector.DoesNotExist):
                sector = None
        else:
            sector = None
        
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        via = request.POST.get('via')
        website = request.POST.get('website')

        partner = None
        referral = None
        
        if via == 'Referral':
            referral = request.POST.get('referral')
            partner_name = None
        elif via == 'Partner':
            partner_id = request.POST.get('partner')
            partner = Partner.objects.filter(id=partner_id).first()

        company = Company(company_name=company_name, sector=sector, address=address, city=city, state=state, country=country, via=via, referral_name=referral, partner_name=partner, website=website, created_by=user)
        company.save()
                
        return HttpResponseRedirect(reverse('company_profile') + f'?company_added=true&company_id={company.id}')
    else:
        return HttpResponse("Form Submission Error!")
    
# New Requirement Request Submission
def add_newrequest(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id=user_id)

    company = Company.objects.filter(created_by=user).first()

    if request.method == 'POST':
        requirement_type = request.POST.get('requirement-category')
        brand_id = request.POST.get('brand') if requirement_type == 'Product' else None
        product_id = request.POST.get('product') if requirement_type == 'Product' else None
        service_id = request.POST.get('service') if requirement_type == 'Service' else None
        requirement_description = request.POST.get('message')

        brand = get_object_or_404(Brand, pk=brand_id) if brand_id else None
        product = get_object_or_404(Product, pk=product_id) if product_id else None
        service = get_object_or_404(Service, pk=service_id) if service_id else None

        Request.objects.create(company=company, date=now(), requirement_type=requirement_type, brand=brand, product_name=product, service=service, requirement_description=requirement_description)

        return redirect(reverse('requirement'))

# Update Requirement Request
@require_POST
def update_request(request):
    if request.method == 'POST':
        request_id = request.POST.get('request-id')
        request_obj = get_object_or_404(Request, id=request_id)

        request_obj.requirement_type = request.POST.get('requirement-category')
        request_obj.service_id = request.POST.get('service')
        request_obj.brand_id = request.POST.get('brand')
        request_obj.product_name_id = request.POST.get('product')
        request_obj.requirement_description = request.POST.get('message')
        request_obj.save()
        messages.success(request, "Request updated successfully.")
        
        return redirect('requirement')

    return redirect('requirement')

# Delete Requirement Request
def delete_request(request, id):
    # Get the request object or raise a 404 error if not found
    request_to_delete = get_object_or_404(Request, id=id)

    if request.method == "POST":
        # Delete the request object
        request_to_delete.delete()
        # Display a success message
        messages.success(request, f"Request '{request_to_delete.requirement_type}' has been deleted.")
        # Redirect to the requirement page or wherever you'd like after deletion
        return redirect('requirement')  # Update with your redirect URL name
    
    # If the request is not POST, redirect to a safe page (e.g., requirement page)
    return redirect('requirement')
    
# New Requirement Submission
def add_newrequirement(request):
    if request.method == 'POST':
        company_id = request.POST.get('company-name')
        contact_id = request.POST.get('contact-person')
        requirement_type = request.POST.get('requirement-category')
        brand_id = request.POST.get('brand') if requirement_type == 'Product' else None
        product_id = request.POST.get('product') if requirement_type == 'Product' else None
        service_id = request.POST.get('service') if requirement_type == 'Service' else None
        requirement_description = request.POST.get('message')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        status = request.POST.get('status') or 'Approved'
        progress = request.POST.get('progress')

        company = get_object_or_404(Company, pk=company_id)
        contact = Contact.objects.filter(pk=contact_id).first() if contact_id else None
        brand = Brand.objects.filter(pk=brand_id).first() if brand_id else None
        product = Product.objects.filter(pk=product_id).first() if product_id else None
        service = Service.objects.filter(pk=service_id).first() if service_id else None

        Requirement.objects.create(company=company, date=now(), contact_name=contact, requirement_type=requirement_type, brand=brand, product_name=product, service=service, requirement_description=requirement_description, currency=currency, price=price, status=status, progress=progress)

        return redirect(reverse('contract'))
    
# New Partner Submission
def add_newpartner(request):
    if 'staff_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        partner_name = request.POST.get('partner-name')

        if Partner.objects.filter(partner_name=partner_name).exists():
            error_message = "Partner with this name already exists!"
            return HttpResponseRedirect(reverse('partner') + f'?add-partner&error_message={error_message}&partner_name={partner_name}')
        
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        contact_name = request.POST.get('contact-name')
        designation = request.POST.get('designation')
        email = request.POST.get('email-address')
        contact_number = request.POST.get('contact-number')

        Partner.objects.create(partner_name=partner_name, address=address, city=city, state=state, country=country, contact_person=contact_name, designation=designation, email=email, phone_number=contact_number)
                
        return redirect(reverse('partner'))
    else:
        return HttpResponse("Form Submission Error!")
    
# New Staff Submission
def add_newstaff(request):
    if request.method == 'POST':
        full_name = request.POST.get('staff-name')
        role = request.POST.get('role')
        email = request.POST.get('email-address')
        password = request.POST.get('password')
        
        if not full_name or not email or not password or not role:
            return redirect('staff')

        if Staff.objects.filter(email=email).exists():
            return redirect('staff')

        try:
            new_staff = Staff(full_name=full_name, role=role, email=email, password=make_password(password))
            new_staff.save()
            messages.success(request, "Staff member added successfully.")
            return redirect('staff')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('add_newstaff')

    return render(request, 'staff.html')

# New Transaction Submission
def add_newtransaction(request):
    if 'staff_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        company = get_object_or_404(Company, id=request.POST.get('company-name'))
        requirement = get_object_or_404(Requirement, id=request.POST.get('requirement'))
        contact = get_object_or_404(Contact, id=request.POST.get('contact-person'))

        Transaction.objects.create(date=request.POST.get('date'), company=company, requirement=requirement, contact=contact, action=request.POST.get('action'), remark=request.POST.get('remarks'))
        return redirect('transaction')

# Add Transaction
def add_transaction(request, company_id, requirement_id):
    if 'staff_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        company = get_object_or_404(Company, id=company_id)
        requirement = get_object_or_404(Requirement, id=requirement_id)
        date = request.POST.get('date')
        contact_id = request.POST.get('contact-person')
        contact = get_object_or_404(Contact, id=contact_id)
        action = request.POST.get('action')
        remark = request.POST.get('remarks')

        Transaction.objects.create(date=date, company=company, requirement=requirement, contact=contact, action=action, remark=remark )
        return redirect('contractdetails', company_id=company_id, requirement_id=requirement_id)
    
# New Sector Submission
def add_newsector(request):
    if 'staff_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        sector_name = request.POST.get('sector-name')

        if Sector.objects.filter(sector_name=sector_name).exists():
            return redirect(reverse('sector'))

        sector = Sector(sector_name=sector_name)
        sector.save()

        return redirect(reverse('sector'))
    else:
        return render(request, 'sector.html')    

# New Service Submission
def add_newservice(request):
    if 'staff_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        service_name = request.POST.get('service-name')

        if Service.objects.filter(service_name=service_name).exists():
            return redirect(reverse('service'))

        service = Service(service_name=service_name)
        service.save()

        return redirect(reverse('service'))
    else:
        return render(request, 'service.html')
    
# New Brand Submission
def add_newbrand(request):
    if 'staff_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        brand_name = request.POST.get('brand-name')

        if Brand.objects.filter(brand_name=brand_name).exists():
            return redirect(reverse('brand'))

        brand = Brand(brand_name=brand_name)
        brand.save()

        return redirect('brand')
    else:
        return render(request, 'brand.html')
    
# Staff Status Toggle
@require_POST
def toggle_staff_status(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    staff.status = not staff.status
    staff.save()
    return JsonResponse({'status': staff.status})

# View Company Details
def companydetails(request, company_id):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = get_object_or_404(Staff, id=staff_id)

    company = get_object_or_404(Company, id=company_id)
    requirements = Requirement.objects.filter(company=company).select_related('brand', 'product_name', 'service').prefetch_related('requirement_transactions')
    contacts = Contact.objects.filter(company=company)
    services = Service.objects.values('id', 'service_name').distinct().order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').distinct().order_by('brand_name')
    products = Product.objects.values('id', 'product_name').distinct().order_by('product_name')

    requirements_count = Requirement.objects.filter(company=company).select_related('brand', 'product_name', 'service').prefetch_related('requirement_transactions')
    requirements_paginator = Paginator(requirements_count, 10)
    requirements_page_number = request.GET.get('requirements_page', 1)
    requirements_page_obj = requirements_paginator.get_page(requirements_page_number)

    context = {'user': user, 'company': company, 'requirements': requirements, 'contacts': contacts, 'services': services, 'brands': brands, 'products': products, 'requirements_page_obj': requirements_page_obj}
    return render(request, 'companydetails.html', context)

# View Contract Details
def contractdetails(request, company_id, requirement_id):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = get_object_or_404(Staff, id=staff_id)
    
    company = get_object_or_404(Company, id=company_id)
    requirement = get_object_or_404(Requirement, id=requirement_id)
    requirements = Requirement.objects.filter(company=company).select_related('brand', 'product_name', 'service').prefetch_related('requirement_transactions')
    transactions = Transaction.objects.filter(company=company, requirement=requirement).order_by('-date')

    transactions_count = Transaction.objects.filter(company=company, requirement=requirement).select_related('date', 'action', 'remark').prefetch_related('transaction_transactions')
    transactions_paginator = Paginator(transactions_count, 10)
    transactions_page_number = request.GET.get('transactions_page', 1)
    transactions_page_obj = transactions_paginator.get_page(transactions_page_number)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        transactions = transactions.filter(date__range=[start_date, end_date])

    contacts = Contact.objects.filter(company=company)
    context = {'user': user, 'company': company, 'requirement': requirement, 'requirements': requirements, 'transactions': transactions, 'transactions_page_obj': transactions_page_obj, 'contacts': contacts}
    return render(request, 'contractdetails.html', context)

# View Requirement Details
def requirementdetails(request, company_id, requirement_id):
    if 'user_id' not in request.session:
        return redirect('login')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id=user_id)
    
    company = get_object_or_404(Company, id=company_id)
    requirement = get_object_or_404(Requirement, id=requirement_id)
    requirements = Requirement.objects.filter(company=company).select_related('brand', 'product_name', 'service').prefetch_related('requirement_transactions')
    transactions = Transaction.objects.filter(company=company, requirement=requirement).order_by('-date')

    transactions_count = Transaction.objects.filter(company=company, requirement=requirement).select_related('date', 'action', 'remark').prefetch_related('transaction_transactions')
    transactions_paginator = Paginator(transactions_count, 10)
    transactions_page_number = request.GET.get('transactions_page', 1)
    transactions_page_obj = transactions_paginator.get_page(transactions_page_number)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        transactions = transactions.filter(date__range=[start_date, end_date])

    contacts = Contact.objects.filter(company=company)
    context = {'user': user, 'company': company, 'requirement': requirement, 'requirements': requirements, 'transactions': transactions, 'transactions_page_obj': transactions_page_obj, 'contacts': contacts}
    return render(request, 'requirementdetails.html', context)

# View Partner Details
def partnerdetails(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    companies = Company.objects.filter(partner_name=partner)

    paginator = Paginator(companies, 10)
    page = request.GET.get('page')
    try:
        paginated_companies = paginator.page(page)
    except PageNotAnInteger:
        paginated_companies = paginator.page(1)
    except EmptyPage:
        paginated_companies = paginator.page(paginator.num_pages)

    company_requirements = []
    for company in companies:
        total_revenue = Requirement.objects.filter(company=company, status='Completed').aggregate(total=Sum('price'))['total'] or 0.00
        pending_revenue = Requirement.objects.filter(company=company, status__in=['Pipeline', 'Initiated']).aggregate(total=Sum('price'))['total'] or 0.00
        
        company_requirements.append({'company': company, 'total_revenue': total_revenue, 'pending_revenue': pending_revenue})

    context = {'partner': partner, 'company_requirements': company_requirements, 'requirements_page_obj': paginated_companies}
    return render(request, 'partnerdetails.html', context)

# Edit Company Details
def companyeditform(request, company_id):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    contacts = Contact.objects.filter(company=company)
    sectors = Sector.objects.all()
    partners = Partner.objects.all()

    countries = ["Nepal", "USA", "India", "Singapore"]
    religions = ["Hinduism", "Buddhism", "Christianity"]
    return render(request, 'companyeditform.html', {'company': company, 'contacts': contacts, 'sectors': sectors, 'partners': partners, 'countries': countries, 'religions': religions})

# Edit Requirement Details
def requirementeditform(request, requirement_id):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = get_object_or_404(Staff, id=staff_id)

    requirement = get_object_or_404(Requirement, id=requirement_id)
    company = requirement.company
    contacts = Contact.objects.filter(company=company)
    services = Service.objects.values('id', 'service_name').distinct().order_by('service_name')
    brands = Brand.objects.values('id', 'brand_name').distinct().order_by('brand_name')
    products = Product.objects.values('id', 'product_name').distinct().order_by('product_name')

    return render(request, 'requirementeditform.html', {'user': user, 'requirement': requirement, 'contacts': contacts, 'services': services, 'brands': brands, 'products': products})

# Edit Partner Details
def partnereditform(request, partner_id):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    partner = Partner.objects.get(pk=partner_id)
    return render(request, 'partnereditform.html', {'partner': partner})

# Update Company
def update_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        company.company_name = request.POST['company_name']
        company.sector_id = request.POST['sector']
        company.address = request.POST['address']
        company.city = request.POST['city']
        company.state = request.POST['state']
        company.country = request.POST['country']
        company.via = request.POST['via']
        company.referral_name = request.POST.get('referral_name', '')
        company.partner_name_id = request.POST.get('partner_name', '')
        company.website = request.POST['website']
        company.save()

        contact_ids = request.POST.getlist('contact_id[]')
        contact_names = request.POST.getlist('contact_name[]')
        designations = request.POST.getlist('designation[]')
        emails = request.POST.getlist('email[]')
        phone_numbers = request.POST.getlist('phone_number[]')
        dobs = request.POST.getlist('dob[]')
        religions = request.POST.getlist('religion[]')

        existing_contacts = set(Contact.objects.filter(company=company).values_list('id', flat=True))
        updated_contacts = set([int(contact_id) for contact_id in contact_ids if contact_id])
        contacts_to_delete = existing_contacts - updated_contacts
        Contact.objects.filter(id__in=contacts_to_delete).delete()

        for i in range(len(contact_names)):
            contact_id = contact_ids[i] if contact_ids[i] else None
            if contact_id:
                contact = Contact.objects.get(id=contact_id, company=company)
            else:
                contact = Contact(company=company)
            contact.contact_name = contact_names[i]
            contact.designation = designations[i]
            contact.email = emails[i]
            contact.phone_number = phone_numbers[i]
            contact.dob = dobs[i] or None
            contact.religion = religions[i]
            contact.save()

        return redirect('company_profile')

    sectors = Sector.objects.all()
    partners = Partner.objects.all()
    contacts = Contact.objects.filter(company=company)

    return render(request, 'companyprofile.html', {'company': company, 'sectors': sectors, 'partners': partners, 'contacts': contacts})

# Add New Requirement
def add_newrequirement(request):
    if request.method == 'POST':
        company_id = request.POST.get('company-name')
        contact_id = request.POST.get('contact-person')
        requirement_type = request.POST.get('requirement-category')
        brand_id = request.POST.get('brand') if requirement_type == 'Product' else None
        product_id = request.POST.get('product') if requirement_type == 'Product' else None
        service_id = request.POST.get('service') if requirement_type == 'Service' else None
        requirement_description = request.POST.get('message')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        status = request.POST.get('status') or 'Approved'
        progress = request.POST.get('progress')

        company = get_object_or_404(Company, pk=company_id)
        contact = Contact.objects.filter(pk=contact_id).first() if contact_id else None
        brand = Brand.objects.filter(pk=brand_id).first() if brand_id else None
        product = Product.objects.filter(pk=product_id).first() if product_id else None
        service = Service.objects.filter(pk=service_id).first() if service_id else None

        Requirement.objects.create(company=company, date=now(), contact_name=contact, requirement_type=requirement_type, brand=brand, product_name=product, service=service, requirement_description=requirement_description, currency=currency, price=price, status=status, progress=progress)

        return redirect('companydetails', company_id=company.id)

# Update Requirement
def update_requirement(request, requirement_id):
    requirement = get_object_or_404(Requirement, id=requirement_id)

    if request.method == 'POST':
        contact_id = request.POST['contact-person']
        contact = get_object_or_404(Contact, id=contact_id)
        requirement.contact_name = contact

        requirement.date = request.POST['date']
        requirement.requirement_type = request.POST['requirement-category']
        requirement.service = get_object_or_404(Service, id=request.POST['service'])
        requirement.brand = get_object_or_404(Brand, id=request.POST['brand'])
        requirement.product_name = get_object_or_404(Product, id=request.POST['product'])
        requirement.requirement_description = request.POST['message']
        requirement.currency = request.POST['currency']
        requirement.price = request.POST['price']
        requirement.progress = request.POST['progress']
        requirement.save()

        return redirect('requirementeditform', requirement_id=requirement.id)

    return redirect('requirementeditform', requirement_id=requirement.id)

# Update Partner
def update_partner(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)

    if request.method == 'POST':
        partner.partner_name = request.POST['partner-name']
        partner.address = request.POST['address']
        partner.city = request.POST['city']
        partner.state = request.POST['state']
        partner.country = request.POST['country']
        partner.contact_person = request.POST['contact-name']
        partner.designation = request.POST['designation']
        partner.email = request.POST['email']
        partner.phone_number = request.POST['contact-number']
        partner.save()

        return redirect('partnereditform', partner_id=partner.id)
    
    return redirect('partnereditform', partner_id=partner.id)

# Update Sector
@require_POST
def update_sector(request):
    sector_id = request.POST.get('sector-id')
    sector_name = request.POST.get('sector-name')
    sector = get_object_or_404(Sector, id=sector_id)

    sector.sector_name = sector_name
    sector.save()

    return redirect('sector')

# Update Service
@require_POST
def update_service(request):
    service_id = request.POST.get('service-id')
    service_name = request.POST.get('service-name')
    service = get_object_or_404(Service, id=service_id)

    service.service_name = service_name
    service.save()

    return redirect('service')

# Update Brand
@require_POST
def update_brand(request):
    brand_id = request.POST.get('brand-id')
    brand_name = request.POST.get('brand-name')
    brand = get_object_or_404(Brand, id=brand_id)

    brand.brand_name = brand_name
    brand.save()

    return redirect('brand')

# Get AJAX Contacts for Transaction Form
def get_contacts(request):
    company_id = request.GET.get('company_id')
    contacts = Contact.objects.filter(company_id=company_id).values('id', 'contact_name')
    return JsonResponse(list(contacts), safe=False)

def get_requirements(request):
    company_id = request.GET.get('company_id')
    requirements = Requirement.objects.filter(company_id=company_id)
    data = []

    for requirement in requirements:
        if requirement.requirement_type == 'Product':
            display_text = f"{requirement.brand.brand_name if requirement.brand else ''} - {requirement.product_name.product_name if requirement.product_name else ''}"
        elif requirement.requirement_type == 'Service':
            display_text = requirement.service.service_name if requirement.service else 'No Service Name'
        else:
            display_text = 'Unknown Requirement'

        data.append({'id': requirement.id, 'requirement_name': display_text})
    
    return JsonResponse(data, safe=False)

# Export Excel File
def export_excel(request, company_id):
    if 'staff_id' not in request.session:
        return redirect('login')

    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return HttpResponse("Company not found.", status=404)

    transactions = Transaction.objects.filter(company_id=company_id).select_related('requirement').order_by('requirement__id', '-date')

    wb = Workbook()
    ws = wb.active
    ws.title = "Company Data"

    # Define styles
    center_alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    left_alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    bold_font = Font(bold=True)
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

    # Add headers for contacts
    headers = ['Company Name', 'Contact Person', 'Email', 'Phone Number']
    ws.append(headers)
    for cell in ws[1]:
        cell.alignment = center_alignment
        cell.font = bold_font
        cell.border = thin_border

    # Add company contact persons
    for contact in company.company_contacts.all():
        ws.append([company.company_name, contact.contact_name, contact.email, contact.phone_number])
        for cell in ws[ws.max_row]:
            cell.border = thin_border

    # Leave a blank row
    ws.append([])
    ws.append(['S.N.', 'Requirement Type', 'Requirement', 'Date', 'Action', 'Remark'])

    for cell in ws[ws.max_row]:
        cell.alignment = center_alignment
        cell.font = bold_font
        cell.border = thin_border

    # Set column widths
    column_widths = {'A': 23, 'B': 30, 'C': 35, 'D': 20, 'E': 50, 'F': 50}
    for column, width in column_widths.items():
        ws.column_dimensions[column].width = width

    # Write transaction data
    last_requirement_id = None
    merge_start_row = ws.max_row + 1
    sn = 1

    for transaction in transactions:
        requirement = transaction.requirement
        requirement_id = requirement.id if requirement else None
        requirement_type = requirement.requirement_type if requirement else ''
        requirement_value = ''

        if requirement_type.lower() == 'product':
            brand = requirement.brand.brand_name if requirement and requirement.brand else ''
            product_name = requirement.product_name.product_name if requirement and requirement.product_name else ''
            if brand and product_name:
                requirement_value = f"{brand} - {product_name}"
        elif requirement_type.lower() == 'service':
            requirement_value = requirement.service.service_name if requirement and requirement.service else ''

        if last_requirement_id and last_requirement_id != requirement_id:
            if ws.max_row - 1 > merge_start_row:
                ws.merge_cells(start_row=merge_start_row, start_column=1, end_row=ws.max_row - 1, end_column=1)
                ws.merge_cells(start_row=merge_start_row, start_column=2, end_row=ws.max_row - 1, end_column=2)
                ws.merge_cells(start_row=merge_start_row, start_column=3, end_row=ws.max_row - 1, end_column=3)
            merge_start_row = ws.max_row + 1

        ws.append([sn, requirement_type, requirement_value, transaction.date, transaction.action, transaction.remark])
        for cell in ws[ws.max_row]:
            cell.alignment = left_alignment if cell.column_letter in ['E', 'F'] else center_alignment
            cell.border = thin_border

        last_requirement_id = requirement_id
        sn += 1

    if ws.max_row >= merge_start_row:
        ws.merge_cells(start_row=merge_start_row, start_column=1, end_row=ws.max_row, end_column=1)
        ws.merge_cells(start_row=merge_start_row, start_column=2, end_row=ws.max_row, end_column=2)
        ws.merge_cells(start_row=merge_start_row, start_column=3, end_row=ws.max_row, end_column=3)

    # Merge cells for company name
    company_name_start_row = 2
    company_name_end_row = company.company_contacts.count() + 1
    ws.merge_cells(start_row=company_name_start_row, start_column=1, end_row=company_name_end_row, end_column=1)
    for row in range(company_name_start_row, company_name_end_row + 1):
        ws[f'A{row}'].alignment = center_alignment
        ws[f'A{row}'].border = thin_border

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{company.company_name} - Report.xlsx"'
    return response

# Linear Regression Call
def predict_revenue(request):
    company_id = Company.objects.first().id
    predicted_revenue = predict_revenue_for_company(company_id)
    return JsonResponse({'predicted_revenue': predicted_revenue[0]})

# Extra Views
def approve_request_view(request, request_id):
    req = get_object_or_404(Request, id=request_id)
    req.approve()
    return redirect('requirement')

def reject_request_view(request, request_id):
    req = get_object_or_404(Request, id=request_id)
    req.reject()
    return redirect('requirement')

def request_list_view(request):
    requests = Request.objects.filter(is_approved=False)
    return render(request, 'requirement.html', {'requests': requests})

def requirement_list_view(request):
    requirements = Requirement.objects.all()
    return render(request, 'requirement.html', {'requirements': requirements})

# AJAX
def add_sector(request):
    if 'user_id' not in request.session:
        return redirect('user')

    if request.method == 'POST':
        sector_name = request.POST.get('sector-name')

        if Sector.objects.filter(sector_name=sector_name).exists():
            return redirect(reverse('company_profile'))

        sector = Sector(sector_name=sector_name)
        sector.save()
        return redirect('company_profile')
    else:
        return render(request, 'companyprofile.html')