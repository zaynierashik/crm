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

        transaction = Transaction(Company_Name=company_name, date=date, action=action)
        transaction.save()

        return redirect(reverse('homepage') + '?success=True')
    else:
        return HttpResponse("Form Submission Error!")

def master(request):
    sectors = Sector.objects.all()
    requirements = Requirement.objects.all()
    vias = Via.objects.all()
    statuses = Status.objects.all()

    selection = request.GET.get('selection', None)
    return render(request, 'master.html', {'sectors': sectors, 'requirements': requirements, 'vias': vias, 'statuses': statuses, 'selection': selection})