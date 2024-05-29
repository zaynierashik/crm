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

def signup(request):
    fullname = request.session.get('fullname')

    if fullname:
        return redirect('index')

    roles = Role.objects.all()
    return render(request, 'signup.html', {'roles': roles})

def submit_signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        role_type = request.POST.get('role-type')

        try:
            role = Role.objects.get(Role_Name=role_type)
        except Role.DoesNotExist:
            return render(request, 'signup.html', {'error_message': 'Role does not exist.'})

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
        return redirect('index')
    
    return render(request, 'login.html')

def submit_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            ss = Staff.objects.get(email=email)
            if check_password(password, ss.password):
                request.session['fullname'] = ss.Full_Name
                return redirect('index')
            else:
                return redirect(reverse('login') + '?success=False')
        except Staff.DoesNotExist:
            return redirect(reverse('login') + '?success=False')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')   

def index(request):
    companies = Company.objects.order_by('Company_Name')
    requirements = Requirement.objects.all()
    services = Service.objects.all()
    brands = Brand.objects.all()
    success = request.GET.get('success')
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
        
    return render(request, 'index.html', {'companies': companies, 'requirements': requirements, 'services': services, 'brands': brands, 'success': success, 'fullname': fullname})

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
        requirement_type = request.POST.get('requirement-type')
        action = request.POST.get('action')
        remark = request.POST.get('remark')

        if requirement_type == 'Product':
            brand = request.POST.get('brand')
            product_name = request.POST.get('product')
            service = None
        elif requirement_type == 'Service':
            service = request.POST.get('service')
            brand = None
            product_name = None
        else:
            return HttpResponse("Invalid requirement type!")

        transaction = Transaction(Company_Name=company_name, date=date, Requirement_Type=requirement_type, brand=brand, Product_Name=product_name, service=service, action=action, 
                                  remark=remark, Created_By=fullname)
        transaction.save()
        return redirect(reverse('index') + '?success=True')
    else:
        return HttpResponse("Form Submission Error!")

def master(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    companies = Company.objects.filter(Created_By=fullname).order_by('Company_Name')
    sectors = Sector.objects.values('Sector_Name')
    services = Service.objects.values('Service_Name').distinct()
    brands = Brand.objects.values('Brand_Name').distinct()
    vias = Via.objects.all()
    statuses = Status.objects.all()
    partners = Partner.objects.all()

    selection = request.GET.get('selection', None)
    return render(request, 'master.html', {'companies': companies, 'sectors': sectors, 'services': services, 'vias': vias, 'statuses': statuses, 'brands': brands, 'partners': partners, 'selection': selection, 'fullname': fullname})

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
    vias = Via.objects.all()
    statuses = Status.objects.all()
    partners = Partner.objects.values('Partner_Name')
    
    return render(request, 'newcompany.html', {'sectors': sectors, 'services': services, 'brands': brands, 'vias': vias, 'statuses': statuses, 'partners': partners})

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
        
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        via_name = request.POST.get('via')
        via = Via.objects.get(Via_Name=via_name)
        
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

        status_name = request.POST.get('status')
        status = Status.objects.get(Status_Name=status_name)

        contact_names = request.POST.getlist('contact_name[]')
        designations = request.POST.getlist('designation[]')
        emails = request.POST.getlist('email[]')
        phone_numbers = request.POST.getlist('number[]')

        company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, currency=currency, price=price, via=via, 
                          status=status, Referral_Name=referral_name, Partner_Name=partner_name, Created_By=fullname)
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
    sectors = Sector.objects.values('Sector_Name')
    services = Service.objects.values('Service_Name').distinct()
    brands = Brand.objects.values('Brand_Name').distinct()
    vias = Via.objects.all()
    partners = Partner.objects.all()
    statuses = Status.objects.all()

    countries = ["Nepal", "USA", "India", "Singapore"]
    currencies = ["NPR", "USD", "SGD", "Riyal"]
    return render(request, 'companyform.html', {'company': company, 'sectors': sectors, 'services': services, 'brands': brands, 'vias': vias, 'partners': partners, 'statuses': statuses, 'countries': countries, 'currencies': currencies})

def submit_company(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        
        company_name = request.POST.get('company')
        sector_name = request.POST.get('sector')
        sector = Sector.objects.get(Sector_Name=sector_name)
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        requirement = request.POST.get('requirement-type')
        requirement_description = request.POST.get('requirement-description')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        via_name = request.POST.get('via')
        via = Via.objects.get(Via_Name=via_name)
        referral_name = request.POST.get('referral_name')
        partner_name = request.POST.get('partner')
        status_name = request.POST.get('status')
        status = Status.objects.get(Status_Name=status_name)

        company.Company_Name = company_name
        company.sector = sector
        company.address = address
        company.city = city
        company.state = state
        company.country = country
        company.Contact_Person = contact_person
        company.designation = designation
        company.email = email
        company.Phone_Number = phone_number
        company.requirement = requirement
        company.Requirement_Description = requirement_description
        company.currency = currency
        company.price = price
        company.via = via
        company.status = status
        
        if requirement == 'Service':
            service_name = request.POST.get('service')
            if service_name:
                try:
                    service = Service.objects.filter(Service_Name=service_name).first()
                    if service:
                        company.service = service
                    else:
                        return HttpResponse("Service does not exist.")
                except Service.DoesNotExist:
                    return HttpResponse("Service does not exist.")
        else:
            company.service = None
        
        if requirement == 'Product':
            brand_name = request.POST.get('brand')
            product_name = request.POST.get('product')
            if brand_name and product_name:
                try:
                    brand = Brand.objects.filter(Brand_Name=brand_name).first()
                    if brand:
                        company.brand = brand
                        company.Product_Name = product_name
                    else:
                        return HttpResponse("Brand does not exist.")
                except Brand.DoesNotExist:
                    return HttpResponse("Brand does not exist.")
        else:
            company.brand = None
            company.Product_Name = None

        if via_name == 'Referral':
            company.Referral_Name = referral_name
            company.Partner_Name = None
        elif via_name == 'Partner' and partner_name:
            try:
                partner = Partner.objects.filter(Partner_Name=partner_name).first()
                if partner:
                    company.Partner_Name = partner
                    company.Referral_Name = None
                else:
                    return HttpResponse("Partner does not exist.")
            except Partner.DoesNotExist:
                return HttpResponse("Partner does not exist.")
        else:
            company.Partner_Name = None
            company.Referral_Name = None

        company.save()
        return redirect(reverse('master') + '?selection=company')
    else:
        return HttpResponse("Form Submission Error!")

def companydetails(request, company_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    transactions = Transaction.objects.filter(Company_Name=company.Company_Name).order_by('-date')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    contacts = Contact.objects.filter(company=company)

    if start_date and end_date:
        filtered_transactions = transactions.filter(date__range=[start_date, end_date])
    else:
        filtered_transactions = transactions

    return render(request, 'companydetails.html', {'company': company, 'transactions': transactions, 'filtered_transactions': filtered_transactions, 'contacts': contacts})

def submit_requirement(request):
    if request.method == 'POST':
        company_name = request.POST.get('company')
        requirement_type = request.POST.get('requirement-type')
        product_name = request.POST.get('product')
        brand_name = request.POST.get('brand')
        service_name = request.POST.get('service')
        requirement_description = request.POST.get('requirement-description')

        try:
            company = Company.objects.get(Company_Name=company_name)
        except Company.DoesNotExist:
            return HttpResponseBadRequest("Company does not exist.")

        requirement = Requirement.objects.create(company=company, Requirement_Type=requirement_type, Product_Name=product_name, Requirement_Description=requirement_description)

        if requirement_type == 'Product':
            if brand_name:
                brand, created = Brand.objects.get_or_create(Brand_Name=brand_name)
                requirement.brand = brand

        elif requirement_type == 'Service':
            if service_name:
                service, created = Service.objects.get_or_create(Service_Name=service_name)
                requirement.service = service

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

def submit_via(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        via_name = request.POST.get('via')

        via = Via(Via_Name=via_name)
        via.save()

        return redirect(reverse('master') + '?selection=via')
    else:
        return HttpResponse("Form Submission Error!")
    
def submit_status(request):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    if request.method == 'POST':
        status_name = request.POST.get('status')

        status = Status(Status_Name=status_name)
        status.save()

        return redirect(reverse('master') + '?selection=status')
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
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        email = request.POST.get('email')

        if partner_name and address and city and country and contact_person and email:
            partner = Partner(
                Partner_Name=partner_name, 
                address=address, 
                city=city, 
                country=country, 
                Contact_Person=contact_person, 
                email=email
            )
            partner.save()
            return JsonResponse({
                'partner_name': partner_name,
                'address': address,
                'city': city,
                'country': country,
                'contact_person': contact_person,
                'email': email
            })
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
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        email = request.POST.get('email')

        if partner_name:
            if not Partner.objects.filter(Partner_Name=partner_name).exists():
                partner = Partner(Partner_Name=partner_name, address=address, city=city, country=country, Contact_Person=contact_person, email=email)
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
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        email = request.POST.get('email')

        partner.Partner_Name = partner_name
        partner.address = address
        partner.city = city
        partner.country = country
        partner.Contact_Person = contact_person
        partner.email = email

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
    transactions = Transaction.objects.filter(Company_Name=company.Company_Name).order_by('-date')
    
    wb = Workbook()
    ws = wb.active
    ws.append(['Date', 'Action', 'Remark'])
    
    for transaction in transactions:
        ws.append([transaction.date, transaction.action, transaction.remark])

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{company.Company_Name}_transactions.xlsx"'
    return response

def export_pdf(request, company_id):
    fullname = request.session.get('fullname')

    if not fullname:
        return redirect('login')
    
    company = Company.objects.get(pk=company_id)
    transactions = Transaction.objects.filter(Company_Name=company.Company_Name).order_by('-date')

    template_path = 'pdftemplate.html'
    context = {'company': company, 'transactions': transactions}
    
    template = get_template(template_path)
    html = template.render(context)

    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{company.Company_Name}_transactions.pdf"'
        return response
    
    return HttpResponse('Error generating PDF', status=500)