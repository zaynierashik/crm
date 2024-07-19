import io
from django.shortcuts import *
from django.http import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.hashers import check_password, make_password
from django.template.loader import get_template
from xhtml2pdf import pisa
from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.utils import *

def signup(request):
    fullname = request.session.get('fullname')

    if fullname:
        return redirect(reverse('master') + '?selection=company')

    return render(request, 'signup.html')

def submit_signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        role = request.POST.get('role-type')

        name_exists = Staff.objects.filter(Full_Name=fullname).exists()
        email_exists = Staff.objects.filter(email=email).exists()

        if name_exists and email_exists:
            return redirect(reverse('signup') + '?success=False&message=Both name and email already exists.')
        elif name_exists:
            return redirect(reverse('signup') + '?success=False&message=Staff with this name already exists.')
        elif email_exists:
            return redirect(reverse('signup') + '?success=False&message=Email already exists.')
        else:
            user = Staff(Full_Name=fullname, email=email, password=hashed_password, role=role)
            user.save()
            return redirect(reverse('signup') + '?success=True')
    else:
        return render(request, 'signup.html')

def login(request):
    fullname = request.session.get('fullname')

    if fullname:
         return redirect(reverse('master') + '?selection=company')
    
    return render(request, 'login.html')

def submit_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            ss = Staff.objects.get(email=email)
            if check_password(password, ss.password):
                request.session['fullname'] = ss.Full_Name
                return redirect(reverse('master') + '?selection=company')
            else:
                return redirect(reverse('login') + '?success=False')
        except Staff.DoesNotExist:
            return redirect(reverse('login') + '?success=False')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')   

def transaction(request):
    companies = Company.objects.order_by('Company_Name')
    contacts = Contact.objects.all()
    requirements = Requirement.objects.all()
    services = Service.objects.all()
    brands = Brand.objects.all()
    success = request.GET.get('success')
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
        
    return render(request, 'transaction.html', {'companies': companies, 'contacts': contacts, 'requirements': requirements, 'services': services, 'brands': brands, 'success': success, 'fullname': fullname})

def get_companydetails(request):
    company_name = request.GET.get('company')
    requirement_type = request.GET.get('requirement_type')
    brand_name = request.GET.get('brand')

    company = get_object_or_404(Company, Company_Name=company_name)

    if requirement_type == 'Product':
        if brand_name:
            products = list(Requirement.objects.filter(company=company, Requirement_Type='Product', brand__Brand_Name=brand_name).values('Product_Name'))
        else:
            products = list(Requirement.objects.filter(company=company, Requirement_Type='Product').values('Product_Name', 'brand__Brand_Name'))
        return JsonResponse({'products': products})
    elif requirement_type == 'Service':
        services = list(Requirement.objects.filter(company=company, Requirement_Type='Service').values('service__Service_Name'))
        return JsonResponse({'services': services})

    return JsonResponse({'error': 'Invalid requirement type'}, status=400)

def submit_transaction(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        date = request.POST.get('date')
        company_name = request.POST.get('company')
        requirement_id = request.POST.get('requirement')
        action = request.POST.get('action')
        remark = request.POST.get('remark')
        contact_name = request.POST.get('contact-name')

        try:
            company = Company.objects.get(Company_Name=company_name)
        except Company.DoesNotExist:
            return HttpResponseBadRequest("Company does not exist.")
        
        try:
            contact = Contact.objects.get(Contact_Name=contact_name)
        except Contact.DoesNotExist:
            return HttpResponseBadRequest("Contact does not exist.")
        
        try:
            requirement = Requirement.objects.get(id=requirement_id)
        except Requirement.DoesNotExist:
            return HttpResponseBadRequest("Requirement does not exist.")

        transaction = Transaction(
            company=company, 
            date=date, 
            requirement=requirement,
            action=action, 
            remark=remark
        )
        transaction.save()
        return redirect(reverse('transaction') + '?success=True')
    else:
        return HttpResponse("Form Submission Error!")

    
# def transactiondetails(request, company_id, requirement_id):
#     company = get_object_or_404(Company, id=company_id)
#     requirement = get_object_or_404(Requirement, id=requirement_id)
#     transactions = Transaction.objects.filter(company=company, Requirement_Type=requirement.Requirement_Type).order_by('-date')

#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     contacts = Contact.objects.filter(company=company)

#     if start_date and end_date:
#         filtered_transactions = transactions.filter(date__range=[start_date, end_date])
#     else:
#         filtered_transactions = transactions

#     context = {'company': company, 'requirement': requirement, 'transactions': transactions, 'contacts': contacts, 'filtered_transactions': filtered_transactions}
#     return render(request, 'transactiondetails.html', context)

def transactiondetails(request, company_id, requirement_id):
    company = get_object_or_404(Company, id=company_id)
    requirement = get_object_or_404(Requirement, id=requirement_id)

    # Filter transactions for the specific company and requirement
    transactions = Transaction.objects.filter(company=company, requirement=requirement).order_by('-date')

    # Filter transactions based on start and end date if provided
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        transactions = transactions.filter(date__range=[start_date, end_date])

    # Retrieve contacts related to the company
    contacts = Contact.objects.filter(company=company)

    context = {
        'company': company,
        'requirement': requirement,
        'transactions': transactions,
        'contacts': contacts
    }
    return render(request, 'transactiondetails.html', context)


def master(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    companies = Company.objects.filter(Created_By=fullname).order_by('Company_Name')
    contacts = Contact.objects.select_related('company').all()
    sectors = Sector.objects.values('Sector_Name').order_by('Sector_Name')
    services = Service.objects.values('id', 'Service_Name').distinct().order_by('Service_Name')
    brands = Brand.objects.values('Brand_Name').distinct().order_by('Brand_Name')
    partners = Partner.objects.all().order_by('Partner_Name')
    cities = Company.objects.values_list('city', flat=True).distinct().order_by('city')

    city_filter = request.GET.get('city', None)
    if city_filter:
        companies = companies.filter(city=city_filter)

    selection = request.GET.get('selection', None)
    return render(request, 'master.html', {'companies': companies, 'contacts': contacts, 'sectors': sectors, 'services': services, 'brands': brands, 'partners': partners, 'cities': cities, 'selection': selection, 'fullname': fullname})

# def get_contacts(request):
#     company_name = request.GET.get('company', None)
#     contacts = Contact.objects.filter(company__Company_Name=company_name).values('Contact_Name')

#     return JsonResponse({'contacts': list(contacts)})

# def get_requirements(request):
#     company_name = request.GET.get('company', None)
#     requirements = Requirement.objects.filter(company__Company_Name=company_name).values('Requirement_Type')

#     return JsonResponse({'requirements': list(requirements)})

def get_requirements(request):
    company_name = request.GET.get('company', None)
    requirements = Requirement.objects.filter(company__Company_Name=company_name).select_related('brand', 'service').values('id', 'Requirement_Type', 'Product_Name', 'service__Service_Name', 'brand__Brand_Name')

    return JsonResponse({'requirements': list(requirements)})






def get_contacts(request):
    company_name = request.GET.get('company', None)
    contacts = Contact.objects.filter(company__Company_Name=company_name).values('Contact_Name')
    return JsonResponse({'contacts': list(contacts)})


@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        try:
            company_name = request.POST.get('company')
            contact_name = request.POST.get('contact_name')
            designation = request.POST.get('designation')
            email = request.POST.get('email')
            phone = request.POST.get('number')
            company = Company.objects.get(Company_Name=company_name)

            if Contact.objects.filter(company=company, Contact_Name=contact_name).exists():
                return JsonResponse({'error': 'A contact with this name already exists for the given company.'}, status=400)

            contact = Contact(company=company, Contact_Name=contact_name, designation=designation, email=email, Phone_Number=phone)
            contact.save()

            return JsonResponse({
                'Contact_Name': contact.Contact_Name,
                'company': company_name
            })
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company does not exist.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    
def newform(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    formtype = request.GET.get('formtype', None)
    return render(request, 'form.html', {'formtype': formtype})

def newcompany(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    sectors = Sector.objects.values('Sector_Name')
    services = Service.objects.values('Service_Name').distinct()
    brands = Brand.objects.values('Brand_Name').distinct()
    partners = Partner.objects.values('Partner_Name')
    
    return render(request, 'newcompany.html', {'sectors': sectors, 'services': services, 'brands': brands, 'partners': partners})

def submit_newcompany(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        company_name = request.POST.get('company')

        if Company.objects.filter(Company_Name=company_name).exists():
            return redirect(reverse('newcompany') + f'?error_message=Company with this name already exists!&company_name={company_name}')

        sector_name = request.POST.get('sector')
        sector = Sector.objects.filter(Sector_Name=sector_name)

        if sector.exists():
            sectors = sector.first()
        else:
            return HttpResponse("Sector not found")
        
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        
        via_name = request.POST.get('via')
        
        if via_name == 'Referral':
            referral_name = request.POST.get('referral_name')
            partner_name = None
        elif via_name == 'Partner':
            partner = request.POST.get('partner')
            partner_name = Partner.objects.filter(Partner_Name=partner).first()
            referral_name = None
        else:
            referral_name = None
            partner_name = None

        contact_names = request.POST.getlist('contact_name[]')
        designations = request.POST.getlist('designation[]')
        emails = request.POST.getlist('email[]')
        phone_numbers = request.POST.getlist('number[]')

        company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, via=via_name, Referral_Name=referral_name, Partner_Name=partner_name, 
                          Created_By=fullname)
        company.save()

        for i in range(len(contact_names)):
            if contact_names[i] and designations[i] and emails[i] and phone_numbers[i]:
                contact_person = Contact(
                    company=company,
                    Contact_Name=contact_names[i],
                    designation=designations[i],
                    email=emails[i],
                    Phone_Number=phone_numbers[i]
                )
                contact_person.save()
                
        return redirect(reverse('master') + '?selection=company&success=True')
    else:
        return HttpResponse("Form Submission Error!")
    
def companyform(request, company_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    contacts = Contact.objects.filter(company=company)
    sectors = Sector.objects.values('Sector_Name')
    partners = Partner.objects.all()

    display_via = ''
    if company.via and company.via == 'Direct':
        display_via = 'Direct'
    elif company.via and company.via == 'Referral' and company.Referral_Name:
        display_via = company.Referral_Name
    elif company.via and company.via == 'Partner' and company.Partner_Name:
        display_via = company.Partner_Name.Partner_Name

    countries = ["Nepal", "USA", "India", "Singapore"]
    return render(request, 'companyform.html', {'company': company, 'contacts': contacts, 'sectors': sectors, 'partners': partners, 'countries': countries, 
                                                'display_via': display_via})

def submit_company(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        
        company.Company_Name = request.POST.get('company')
        sector_name = request.POST.get('sector')
        company.sector = get_object_or_404(Sector, Sector_Name=sector_name)
        company.address = request.POST.get('address')
        company.city = request.POST.get('city')
        company.state = request.POST.get('state')
        company.country = request.POST.get('country')

        company.save()
        company.contact_persons.all().delete()

        contact_names = request.POST.getlist('contact_name[]')
        designations = request.POST.getlist('designation[]')
        emails = request.POST.getlist('email[]')
        phone_numbers = request.POST.getlist('number[]')

        for name, designation, email, phone_number in zip(contact_names, designations, emails, phone_numbers):
            if name and designation and email and phone_number:
                Contact.objects.create(
                    company=company,
                    Contact_Name=name,
                    designation=designation,
                    email=email,
                    Phone_Number=phone_number
                )

        return redirect(reverse('master') + '?selection=company')
    else:
        return HttpResponse("Form Submission Error!")

def companydetails(request, company_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    requirements = Requirement.objects.filter(company_id=company_id)
    transactions = Transaction.objects.filter(company_id=company_id).order_by('-date')
    contacts = Contact.objects.filter(company=company)

    return render(request, 'companydetails.html', {'company': company, 'requirements': requirements, 'transactions': transactions, 'contacts': contacts})

def submit_requirement(request):
    if request.method == 'POST':
        company_name = request.POST.get('company')
        contact_name = request.POST.get('contact-name')
        requirement_type = request.POST.get('requirement-type')
        product_name = request.POST.get('product')
        brand_name = request.POST.get('brand')
        service_name = request.POST.get('service')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        status = request.POST.get('status')
        requirement_description = request.POST.get('requirement-description')

        try:
            company = Company.objects.get(Company_Name=company_name)
        except Company.DoesNotExist:
            return HttpResponseBadRequest("Company does not exist.")
        
        try:
            contact = Contact.objects.get(Contact_Name=contact_name)
        except Contact.DoesNotExist:
            return HttpResponseBadRequest("Contact does not exist.")

        requirement = Requirement.objects.create(company=company, Contact_Name=contact, Requirement_Type=requirement_type, Product_Name=product_name, currency=currency, 
                                                 price=price, status=status, Requirement_Description=requirement_description)

        if requirement_type == 'Product':
            if brand_name:
                brand, created = Brand.objects.get_or_create(Brand_Name=brand_name)
                requirement.brand = brand

        elif requirement_type == 'Service':
            if service_name:
                service, created = Service.objects.get_or_create(Service_Name=service_name)
                requirement.service = service
                requirement.Product_Name = None

        requirement.save()

        return redirect(reverse('master') + '?selection=requirement&success=True')
    else:
        return HttpResponseBadRequest("Invalid request method.")

@csrf_exempt
def submit_sector(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        sector_name = request.POST.get('sector')
        
        if sector_name:
            sector = Sector(Sector_Name=sector_name)
            sector.save()
            return JsonResponse({'sector_name': sector_name})
    else:
        return HttpResponse("Form Submission Error!")
    
def add_sector(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        sector_name = request.POST.get('sector')
        
        if sector_name:
            if not Sector.objects.filter(Sector_Name=sector_name).exists():
                sector = Sector(Sector_Name=sector_name)
                sector.save()
                return redirect(reverse('master') + '?selection=sector')
            else:
                return render(request, 'form.html', {
                    'error_message': 'Sector already exists!',
                    'sector_name': sector_name,
                    'formtype': 'sector'
                })
        else:
            return render(request, 'form.html', {
                'error_message': 'Sector name cannot be empty!',
                'sector_name': sector_name,
                'formtype': 'sector'
            })
    else:
        return HttpResponse("Form Submission Error!")
    
@csrf_exempt
def submit_service(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        service_name = request.POST.get('service')
        
        if service_name:
            service = Service(Service_Name=service_name)
            service.save()
            return JsonResponse({'service_name': service_name})
    else:
        return HttpResponse("Form Submission Error!")
    
def add_service(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        service_name = request.POST.get('service')
        
        if service_name:
            if not Service.objects.filter(Service_Name=service_name).exists():
                service = Service(Service_Name=service_name)
                service.save()
                return redirect(reverse('master') + '?selection=service')
            else:
                return render(request, 'form.html', {
                    'error_message': 'Service already exists!',
                    'service_name': service_name,
                    'formtype': 'service'
                })
        else:
            return render(request, 'form.html', {
                'error_message': 'Service name cannot be empty!',
                'service_name': service_name,
                'formtype': 'service'
            })
    else:
        return HttpResponse("Form Submission Error!")
    
def update_service(request):
    if request.method == 'POST':
        service_id = request.POST.get('serviceId')
        service_name = request.POST.get('serviceName')

        try:
            service = Service.objects.get(id=service_id)
            service.Service_Name = service_name
            service.save()
            return redirect(reverse('master') + '?selection=service')
        except Service.DoesNotExist:
            return redirect(reverse('master') + '?selection=service')

    return redirect(reverse('master') + '?selection=service')
    
@csrf_exempt
def submit_brand(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        brand_name = request.POST.get('brand')
        
        if brand_name:
            brand = Brand(Brand_Name=brand_name)
            brand.save()
            return JsonResponse({'brand_name': brand_name})
    else:
        return HttpResponse("Form Submission Error!")
    
def add_brand(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        brand_name = request.POST.get('brand')
        
        if brand_name:
            if not Brand.objects.filter(Brand_Name=brand_name).exists():
                brand = Brand(Brand_Name=brand_name)
                brand.save()
                return redirect(reverse('master') + '?selection=brand')
            else:
                return render(request, 'form.html', {
                    'error_message': 'Brand already exists!',
                    'brand_name': brand_name,
                    'formtype': 'brand'
                })
        else:
            return render(request, 'form.html', {
                'error_message': 'Brand name cannot be empty!',
                'brand_name': brand_name,
                'formtype': 'brand'
            })
    else:
        return HttpResponse("Form Submission Error!")
    
def newpartner(request):
    return render(request, 'newpartner.html')

@csrf_exempt
def submit_newpartner(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')

    if request.method == 'POST':
        partner_name = request.POST.get('partner')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        number = request.POST.get('number')

        if partner_name and address and city and country and contact_person and designation and email and number:
            if Partner.objects.filter(Partner_Name=partner_name).exists():
                return JsonResponse({'error': 'A partner with this name already exists.'}, status=400)

            partner = Partner(Partner_Name=partner_name, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation, email=email, Phone_Number=number)
            partner.save()

            return JsonResponse({'partner_name': partner_name, 'address': address, 'city': city, 'state':state, 'country': country, 'contact_person': contact_person, 'designation': designation, 'email': email, 'number': number})
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        return HttpResponse("Form Submission Error!", status=405)
    
def add_newpartner(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        partner_name = request.POST.get('partner')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        number = request.POST.get('number')

        if partner_name:
            if not Partner.objects.filter(Partner_Name=partner_name).exists():
                partner = Partner(Partner_Name=partner_name, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation, email=email, Phone_Number=number)
                partner.save()
                return redirect(reverse('master') + '?selection=partner')
            else:
                return render(request, 'newpartner.html', {
                    'error_message': 'Partner already exists!',
                    'partner_name': partner_name,
                })
        else:
            return render(request, 'newpartner.html', {
                'error_message': 'Partner name cannot be empty!',
                'partner_name': partner_name,
            })
    else:
        return redirect(reverse('master') + '?selection=partner')
    
def partnerform(request, partner_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    partner = Partner.objects.get(pk=partner_id)
    return render(request, 'partnerform.html', {'partner': partner})
    
def submit_partner(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        partner_id = request.POST.get('partner_id')
        partner = get_object_or_404(Partner, id=partner_id)

        partner_name = request.POST.get('partner')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        number = request.POST.get('number')

        partner.Partner_Name = partner_name
        partner.address = address
        partner.city = city
        partner.state = state
        partner.country = country
        partner.Contact_Person = contact_person
        partner.designation = designation
        partner.email = email
        partner.Phone_Number = number

        partner.save()
        return redirect(reverse('master') + '?selection=partner')
    else:
        return HttpResponse("Form Submission Error!")

def partnerdetails(request, partner_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    partner = Partner.objects.get(pk=partner_id)
    partners = Partner.objects.all()
    return render(request, 'partnerdetails.html', { 'partner': partner, 'partners': partners})
    
def export_excel(request, company_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    transactions = Transaction.objects.filter(company_id=company_id).order_by('-date')
    
    wb = Workbook()
    ws = wb.active
    ws.append(['Date', 'Requirement Type', 'Brand', 'Product Name', 'Service', 'Action', 'Remark'])

    column_widths = {'A': 15, 'B': 17, 'C': 25, 'D': 25, 'E': 35, 'F': 35, 'G': 35}
    for column, width in column_widths.items():
        ws.column_dimensions[column].width = width

    date_style = NamedStyle(name='date_style', number_format='YYYY-MM-DD')
    for cell in ws['A']:
        cell.style = date_style

    center_alignment = Alignment(horizontal='center', vertical='center')
    wrap_text_alignment = Alignment(wrap_text=True, vertical='center')
    
    for cell in ws[1]:
        cell.alignment = center_alignment

    for row_num, transaction in enumerate(transactions, start=2):
        brand = transaction.brand.Brand_Name if transaction.brand else ''
        service = transaction.service.Service_Name if transaction.service else ''
        ws.append([
            transaction.date,
            transaction.Requirement_Type,
            brand,
            transaction.Product_Name,
            service,
            transaction.action,
            transaction.remark
        ])

        for col in ['E', 'F', 'G']:
            ws[f'{col}{row_num}'].alignment = wrap_text_alignment
        
        for col in ['A', 'B', 'C', 'D']:
            ws[f'{col}{row_num}'].alignment = center_alignment

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{company.Company_Name} Transactions.xlsx"'
    return response

def export_pdf(request, company_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    transactions = Transaction.objects.filter(company_id=company_id).order_by('-date')
    contacts = Contact.objects.filter(company=company)

    template_path = 'pdftemplate.html'
    context = {'company': company, 'transactions': transactions, 'contacts': contacts}
    template = get_template(template_path)
    html = template.render(context)

    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{company.Company_Name} Transactions.pdf"'
        return response
    
    return HttpResponse('Error generating PDF', status=500)