from django.shortcuts import *
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    companies = Company.objects.all()
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
    companies = Company.objects.all()
    sectors = Sector.objects.all()
    services = Service.objects.all()
    vias = Via.objects.all()
    statuses = Status.objects.all()
    brands = Brand.objects.all()
    partners = Partner.objects.all()

    selection = request.GET.get('selection', None)
    return render(request, 'master.html', {'companies': companies, 'sectors': sectors, 'services': services, 'vias': vias, 'statuses': statuses, 'brands': brands, 'partners': partners, 'selection': selection})

def newform(request):
    formtype = request.GET.get('formtype', None)
    return render(request, 'form.html', {'formtype': formtype})

def companyform(request, company_id):
    company = Company.objects.get(pk=company_id)
    sectors = Sector.objects.all()
    services = Service.objects.all()
    brands = Brand.objects.all()
    vias = Via.objects.all()
    partners = Partner.objects.all()
    statuses = Status.objects.all()
    return render(request, 'companyform.html', {'company': company, 'sectors': sectors, 'services': services, 'brands': brands, 'vias': vias, 'partners': partners, 'statuses': statuses})

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
        service_name = request.POST.get('service')
        service = Service.objects.get(Service_Name=service_name)
        requirement_description = request.POST.get('requirement-description')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        via_name = request.POST.get('via')
        via = Via.objects.get(Via_Name=via_name)
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
        company.service = service
        company.Requirement_Description = requirement_description
        company.currency = currency
        company.price = price
        company.via = via
        company.status = status
        
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

def submit_sector(request):
    if request.method == 'POST':
        sector_name = request.POST.get('sector')

        # Save sector to database
        sector = Sector(Sector_Name=sector_name)
        sector.save()

        if request.is_ajax():
            # If the request is AJAX, return JSON response with newly added sector data
            return JsonResponse({'id': sector.id, 'Sector_Name': sector.Sector_Name})
        else:
            # If not AJAX, redirect to the appropriate page
            return redirect(reverse('master') + '?selection=sector')
    else:
        return HttpResponse("Form Submission Error!")
    
def submit_service(request):
    if request.method == 'POST':
        service_name = request.POST.get('service')

        service = Service(Service_Name=service_name)
        service.save()

        return redirect(reverse('master') + '?selection=service')
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
    
def submit_brand(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand')

        brand = Brand(Brand_Name=brand_name)
        brand.save()

        return redirect(reverse('master') + '?selection=brand')
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

def newcompany(request):
    sectors = Sector.objects.all()
    services = Service.objects.all()
    brands = Brand.objects.all()
    vias = Via.objects.all()
    statuses = Status.objects.all()
    partners = Partner.objects.all()
    return render(request, 'newcompany.html', {'sectors': sectors, 'services': services, 'brands': brands, 'vias': vias, 'statuses': statuses, 'partners': partners})

def submit_newcompany(request):
    if request.method == 'POST':
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
        
        requirement_description = request.POST.get('requirement-description')
        currency = request.POST.get('currency')
        price = request.POST.get('price')
        via_name = request.POST.get('via')
        via = Via.objects.get(Via_Name=via_name)

        requirement_type = request.POST.get('requirement-type')
        if requirement_type == 'Product':
            brand_name = request.POST.get('brand')
            brand = Brand.objects.get(Brand_Name=brand_name)
            service = None
        elif requirement_type == 'Service':
            service_name = request.POST.get('service')
            service = Service.objects.get(Service_Name=service_name)
            brand = None
        
        if via_name == 'Referral':
            referral_name = request.POST.get('referral_name')
        elif via_name == 'Partner':
            partner_id = request.POST.get('partner')
            partner_name = Partner.objects.get(pk=partner_id)
        else:
            referral_name = None

        status_name = request.POST.get('status')
        status = Status.objects.get(Status_Name=status_name)

        if requirement_type == 'Product':
            company = Company(Company_Name=company_name, sector=sector, address=address, city=city, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Referral_Name=referral_name)
        elif requirement_type == 'Service':
            company = Company(Company_Name=company_name, sector=sector, address=address, city=city, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, service=service, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Partner_Name=partner_name)
        
        if via_name == 'Referral':
            company = Company(Company_Name=company_name, sector=sector, address=address, city=city, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, service=service, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Referral_Name=referral_name)
        elif via_name == 'Partner':
            company = Company(Company_Name=company_name, sector=sector, address=address, city=city, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, service=service, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status, Partner_Name=partner_name)
        else:
            company = Company(Company_Name=company_name, sector=sector, address=address, city=city, country=country, Contact_Person=contact_person, designation=designation,
                             email=email, Phone_Number=phone_number, service=service, brand=brand, Requirement_Description=requirement_description,
                             currency=currency, price=price, via=via, status=status)
            
        company.save()
        return redirect(reverse('master') + '?selection=company')
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