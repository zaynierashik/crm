import io
from django.shortcuts import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa
from openpyxl import Workbook

def index(request):
    companies = Company.objects.order_by('Company_Name')
    success = request.GET.get('success')
    return render(request, 'index.html', {'companies': companies, 'success': success})

def submit_transaction(request):
    if request.method == 'POST':
        company_name = request.POST.get('company')
        date = request.POST.get('date')
        action = request.POST.get('action')
        remark = request.POST.get('remark')

        transaction = Transaction(Company_Name=company_name, date=date, action=action, remark=remark)
        transaction.save()
        return redirect(reverse('index') + '?success=True')
    else:
        return HttpResponse("Form Submission Error!")

def master(request):
    companies = Company.objects.order_by('Company_Name')
    sectors = Sector.objects.values('Sector_Name')
    services = Service.objects.values('Service_Name')
    brands = Brand.objects.values('Brand_Name')
    vias = Via.objects.all()
    statuses = Status.objects.all()
    partners = Partner.objects.all()

    selection = request.GET.get('selection', None)
    return render(request, 'master.html', {'companies': companies, 'sectors': sectors, 'services': services, 'vias': vias, 'statuses': statuses, 'brands': brands, 'partners': partners, 'selection': selection})

def newform(request):
    formtype = request.GET.get('formtype', None)
    return render(request, 'form.html', {'formtype': formtype})

def newcompany(request):
    sectors = Sector.objects.values('Sector_Name')
    services = Service.objects.values('Service_Name')
    brands = Brand.objects.values('Brand_Name')
    vias = Via.objects.all()
    statuses = Status.objects.all()
    partners = Partner.objects.all()
    
    return render(request, 'newcompany.html', {'sectors': sectors, 'services': services, 'brands': brands, 'vias': vias, 'statuses': statuses, 'partners': partners})

def submit_newcompany(request):
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
        contact_person = request.POST.get('contact')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        requirement_description = request.POST.get('requirement-description')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        via_name = request.POST.get('via')
        via = Via.objects.get(Via_Name=via_name)

        requirement_type = request.POST.get('requirement-type')
        if requirement_type == 'Product':
            product_name = request.POST.get('product')
            brand_name = request.POST.get('brand')
            brand = Brand.objects.filter(Brand_Name=brand_name).first()
            service = None
        elif requirement_type == 'Service':
            service_name = request.POST.get('service')
            service = Service.objects.filter(Service_Name=service_name).first()
            product_name = None
            brand = None
        
        if via_name == 'Referral':
            referral_name = request.POST.get('referral_name')
            partner_name = None
        elif via_name == 'Partner':
            partner_id = request.POST.get('partner')
            partner_name = Partner.objects.get(pk=partner_id)
            referral_name = None
        else:
            referral_name = None
            partner_name = None

        status_name = request.POST.get('status')
        status = Status.objects.get(Status_Name=status_name)

        if requirement_type == 'Product':
            company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, requirement=requirement_type, Product_Name=product_name, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Referral_Name=referral_name)
        elif requirement_type == 'Service':
            company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, requirement=requirement_type, service=service, Product_Name=product_name, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Partner_Name=partner_name)
        
        if via_name == 'Referral':
            company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, requirement=requirement_type, service=service, Product_Name=product_name, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Referral_Name=referral_name)
        elif via_name == 'Partner':
            company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, requirement=requirement_type, service=service, Product_Name=product_name, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Partner_Name=partner_name)
        else:
            company = Company(Company_Name=company_name, sector=sectors, address=address, city=city, state=state, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, requirement=requirement_type, service=service, Product_Name=product_name, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status)
            
        company.save()
        return redirect(reverse('master') + '?selection=company')
    else:
        return HttpResponse("Form Submission Error!")
    
def companyform(request, company_id):
    company = Company.objects.get(pk=company_id)
    sectors = Sector.objects.values('Sector_Name')
    services = Service.objects.values('Service_Name')
    brands = Brand.objects.values('Brand_Name')
    vias = Via.objects.all()
    partners = Partner.objects.all()
    statuses = Status.objects.all()

    countries = ["Nepal", "USA", "India", "Singapore"]
    currencies = ["NPR", "USD", "SGD", "Riyal"]
    return render(request, 'companyform.html', {'company': company, 'sectors': sectors, 'services': services, 'brands': brands, 'vias': vias, 'partners': partners, 'statuses': statuses, 'countries': countries, 'currencies': currencies})

def submit_company(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        
        company_name = request.POST.get('company')
        sector_name = request.POST.get('sector')
        sector = Sector.objects.get(Sector_Name=sector_name)
        address = request.POST.get('address')
        city = request.POST.get('city')
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
        company.Referral_Name = referral_name
        company.Partner_Name = partner_name
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
            if brand_name:
                try:
                    brand = Brand.objects.filter(Brand_Name=brand_name).first()
                    if brand:
                        company.brand = brand
                    else:
                        return HttpResponse("Brand does not exist.")
                except Brand.DoesNotExist:
                    return HttpResponse("Brand does not exist.")
        else:
            company.brand = None

        if via_name == 'Referral':
            referral_name = request.POST.get('referral_name')
            company.Referral_Name = referral_name
            company.partner = None
        elif via_name == 'Partner':
            partner_name = request.POST.get('partner')
            if partner_name:
                try:
                    partner = Partner.objects.filter(Partner_Name=partner_name).first()
                    if partner:
                        company.partner = partner
                        company.Referral_Name = None
                    else:
                        return HttpResponse("Partner does not exist.")
                except Partner.DoesNotExist:
                    return HttpResponse("Partner does not exist.")
        else:
            company.partner = None
            company.Referral_Name = None

        company.save()
        return redirect(reverse('master') + '?selection=company')
    else:
        return HttpResponse("Form Submission Error!")

def companydetails(request, company_id):
    company = Company.objects.get(pk=company_id)
    transactions = Transaction.objects.filter(Company_Name=company.Company_Name).order_by('-date')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        filtered_transactions = transactions.filter(date__range=[start_date, end_date])
    else:
        filtered_transactions = transactions

    return render(request, 'companydetails.html', {'company': company, 'transactions': transactions, 'filtered_transactions': filtered_transactions})

@csrf_exempt
def submit_sector(request):
    if request.method == 'POST':
        sector_name = request.POST.get('sector')
        
        if sector_name:
            sector = Sector(Sector_Name=sector_name)
            sector.save()
            return JsonResponse({'sector_name': sector_name})
    else:
        return HttpResponse("Form Submission Error!")
    
def add_sector(request):
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
    if request.method == 'POST':
        service_name = request.POST.get('service')
        
        if service_name:
            service = Service(Service_Name=service_name)
            service.save()
            return JsonResponse({'service_name': service_name})
    else:
        return HttpResponse("Form Submission Error!")
    
def add_service(request):
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
    if request.method == 'POST':
        brand_name = request.POST.get('brand')
        
        if brand_name:
            brand = Brand(Brand_Name=brand_name)
            brand.save()
            return JsonResponse({'brand_name': brand_name})
    else:
        return HttpResponse("Form Submission Error!")
    
def add_brand(request):
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
    if request.method == 'POST':
        via_name = request.POST.get('via')

        via = Via(Via_Name=via_name)
        via.save()

        return redirect(reverse('master') + '?selection=via')
    else:
        return HttpResponse("Form Submission Error!")
    
def submit_status(request):
    if request.method == 'POST':
        status_name = request.POST.get('status')

        status = Status(Status_Name=status_name)
        status.save()

        return redirect(reverse('master') + '?selection=status')
    else:
        return HttpResponse("Form Submission Error!")
    
def newpartner(request):
    return render(request, 'newpartner.html')

def submit_newpartner(request):
    if request.method == 'POST':
        partner_name = request.POST.get('partner')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        contact_person = request.POST.get('contact')
        email = request.POST.get('email')
        partner = Partner(Partner_Name=partner_name, address=address, city=city, country=country, Contact_Person=contact_person, email=email)
        
        partner.save()
        return redirect(reverse('master') + '?selection=partner')
    else:
        return HttpResponse("Form Submission Error!")
    
def partnerform(request, partner_id):
    partner = Partner.objects.get(pk=partner_id)
    return render(request, 'partnerform.html', {'partner': partner})
    
def submit_partner(request):
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
    partner = Partner.objects.get(pk=partner_id)
    partners = Partner.objects.all()
    return render(request, 'partnerdetails.html', { 'partner': partner, 'partners': partners})
    
def export_excel(request, company_id):
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