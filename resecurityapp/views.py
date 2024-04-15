from django.shortcuts import *
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        print("Already logged in.")
        return redirect('index')
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print("email or password is incorrect")
            msg = "email or password is incorrect"
            return render(request, "index.html", {'message': msg})
    return render(request, 'index.html', {})

def homepage(request):
    companies = Company.objects.all()
    success = request.GET.get('success')
    return render(request, 'homepage.html', {'companies': companies, 'success': success})

def submit_transaction(request):
    if request.method == 'POST':
        company_name = request.POST.get('company')
        date = request.POST.get('date')
        action = request.POST.get('action')
        remark = request.POST.get('remark')

        transaction = Transaction(Company_Name=company_name, date=date, action=action, remark=remark)
        transaction.save()

        return redirect(reverse('homepage') + '?success=True')
    else:
        return HttpResponse("Form Submission Error!")

def master(request):
    companies = Company.objects.all()
    sectors = Sector.objects.all()
    requirements = Requirement.objects.all()
    vias = Via.objects.all()
    statuses = Status.objects.all()
    partners = Partner.objects.all()

    selection = request.GET.get('selection', None)
    return render(request, 'master.html', {'companies': companies, 'sectors': sectors, 'requirements': requirements, 'vias': vias, 'statuses': statuses, 'partners': partners, 'selection': selection})

def submit_company(request):
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
        requirement_name = request.POST.get('requirement')
        requirement = Requirement.objects.get(Requirement_Name=requirement_name)
        requirement_description = request.POST.get('requirement-description')
        price = request.POST.get('price')
        via_name = request.POST.get('via')
        via = Via.objects.get(Via_Name=via_name)
        status_name = request.POST.get('status')
        status = Status.objects.get(Status_Name=status_name)

        company = Company(Company_Name=company_name, sector=sector, address=address, city=city, country=country, Contact_Person=contact_person, designation=designation,
                         email=email, Phone_Number=phone_number, requirement=requirement, Requirement_Description=requirement_description, price=price, via=via, status=status)
        company.save()

        return redirect(reverse('master') + '?selection=company')
    else:
        return HttpResponse("Form Submission Error!")

def submit_sector(request):
    if request.method == 'POST':
        sector_name = request.POST.get('sector')

        sector = Sector(Sector_Name=sector_name)
        sector.save()

        return redirect(reverse('master') + '?selection=sector')
    else:
        return HttpResponse("Form Submission Error!")
    
def submit_requirement(request):
    if request.method == 'POST':
        requirement_name = request.POST.get('requirement')

        requirement = Requirement(Requirement_Name=requirement_name)
        requirement.save()

        return redirect(reverse('master') + '?selection=requirement')
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
    
def submit_partner(request):
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
    
def companyform(request, company_id):
    company = Company.objects.get(pk=company_id)
    sectors = Sector.objects.all()
    requirements = Requirement.objects.all()
    vias = Via.objects.all()
    statuses = Status.objects.all()
    return render(request, 'companyform.html', {'company': company, 'sectors': sectors, 'requirements': requirements, 'vias': vias, 'statuses': statuses})

def companydetails(request, company_id):
    company = Company.objects.get(pk=company_id)
    transactions = Transaction.objects.filter(Company_Name=company.Company_Name)
    return render(request, 'companydetails.html', {'company': company, 'transactions': transactions})

def partnerform(request, partner_id):
    partners = Partner.objects.get(pk=partner_id)
    return render(request, 'partnerform.html', {'partners': partners})

def partnerdetails(request, partner_id):
    partner = Partner.objects.get(pk=partner_id)
    partners = Partner.objects.all()
    return render(request, 'partnerdetails.html', { 'partner': partner, 'partners': partners})