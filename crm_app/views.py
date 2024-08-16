from django.shortcuts import render, redirect, get_object_or_404
from django.http import *
from django.urls import reverse
from .models import *
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout, update_session_auth_hash

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

        request.session.set_expiry(3600)
        return redirect('dashboard')

    return render(request, 'login.html')

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

    context = {'companies': companies, 'contacts': contacts, 'sectors': sectors, 'services': services, 'brands': brands, 'products': products, 
               'partners': partners, 'cities': cities, 'staffs': staffs, 'company_count': company_count, 'companies': companies_page, 'paginator': paginator, 'page_obj': companies_page, 'user': user}

    return render(request, 'index.html', context)

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
        companies = companies.filter(city=city_filter)

    if status_filter:
        status_value = status_filter.lower() == 'active'
        companies = companies.filter(status=status_value)

    paginator_active = Paginator(active_companies, 10)  # 10 items per page
    page_active = request.GET.get('page_active')

    try:
        active_companies_page = paginator_active.page(page_active)
    except PageNotAnInteger:
        active_companies_page = paginator_active.page(1)
    except EmptyPage:
        active_companies_page = paginator_active.page(paginator_active.num_pages)

    paginator_inactive = Paginator(inactive_companies, 10)  # 10 items per page
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

def requirement(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    return render(request, 'requirement.html', {'user': user})

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

    company_count = Company.objects.count()
    initiated_count = Requirement.objects.filter(status="Initiated").count()
    pipeline_count = Requirement.objects.filter(status="Pipeline").count()
    completed_count = Requirement.objects.filter(status="Completed").count()

    city_filter = request.GET.get('city', None)
    status_filter = request.GET.get('status', 'active')

    if city_filter:
        companies = companies.filter(city=city_filter)

    if status_filter:
        status_value = status_filter.lower() == 'active'
        companies = companies.filter(status=status_value)

    paginator = Paginator(companies, 10)
    page = request.GET.get('page')

    try:
        companies_page = paginator.page(page)
    except PageNotAnInteger:
        companies_page = paginator.page(1)
    except EmptyPage:
        companies_page = paginator.page(paginator.num_pages)

    context = {'companies': companies, 'contacts': contacts, 'sectors': sectors, 'services': services, 'brands': brands, 'products': products, 
               'partners': partners, 'cities': cities, 'staffs': staffs, 'company_count': company_count, 'initiated_count': initiated_count, 'pipeline_count': pipeline_count, 
               'completed_count': completed_count, 'companies': companies_page, 'paginator': paginator, 'page_obj': companies_page, 'user': user}

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

# New Company Submission
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
    
# New Partner Submission
def add_newpartner(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

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

        partner = Partner(partner_name=partner_name, address=address, city=city, state=state, country=country, contact_person=contact_name, designation=designation, email=email, phone_number=contact_number)
        partner.save()
                
        return redirect(reverse('partner'))
    else:
        return HttpResponse("Form Submission Error!")
    
# New Staff Submission
def add_newstaff(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    if request.method == 'POST':
        full_name = request.POST.get('staff-name')
        role = request.POST.get('role')
        email = request.POST.get('email-address')
        password = request.POST.get('password')
        
        if not full_name or not email or not password or not role:
            error_message = "All fields are required!"
            return HttpResponseRedirect(reverse('add_newstaff') + f'?error_message={error_message}')

        if Staff.objects.filter(email=email).exists():
            error_message = "Email is already in use!"
            return HttpResponseRedirect(reverse('add_newstaff') + f'?error_message={error_message}')

        try:
            new_staff = Staff(full_name=full_name, role=role, email=email, password=make_password(password))
            new_staff.save()
            messages.success(request, "Staff member added successfully.")
            return redirect('staff')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('add_newstaff')

    return render(request, 'staff.html')
    
# New Sector Submission
def add_newsector(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

    if request.method == 'POST':
        sector_name = request.POST.get('sector-name')

        if Sector.objects.filter(sector_name=sector_name).exists():
            return redirect(reverse('sector'))

        sector = Sector(sector_name=sector_name)
        sector.save()

        return redirect('sector')
    else:
        return render(request, 'sector.html')
    
# New Service Submission
def add_newservice(request):
    if 'staff_id' not in request.session:
        return redirect('login')
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

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
    
    staff_id = request.session.get('staff_id')
    user = Staff.objects.get(id=staff_id)

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