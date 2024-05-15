"""
URL configuration for resecurity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from resecurityapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('master/', views.master, name='master'),
    path('newform/', views.newform, name='newform'),
    path('submit_transaction/', views.submit_transaction, name='submit_transaction'),
    path('submit_company/', views.submit_company, name='submit_company'),
    path('submit_sector/', views.submit_sector, name='submit_sector'),
    path('submit_service/', views.submit_service, name='submit_service'),
    path('submit_via/', views.submit_via, name='submit_via'),
    path('submit_status/', views.submit_status, name='submit_status'),
    path('submit_brand/', views.submit_brand, name='submit_brand'),
    path('submit_partner/', views.submit_partner, name='submit_partner'),
    path('companyform/<int:company_id>/', views.companyform, name='companyform'),
    path('companydetails/<int:company_id>/', views.companydetails, name='companydetails'),
    path('partnerform/<int:partner_id>/', views.partnerform, name='partnerform'),
    path('partnerdetails/<int:partner_id>/', views.partnerdetails, name='partnerdetails'),
    path('newcompany/', views.newcompany, name='newcompany'),
    path('submit_newcompany/', views.submit_newcompany, name='submit_newcompany'),
    path('newpartner/', views.newpartner, name='newpartner'),
    path('submit_newpartner/', views.submit_newpartner, name='submit_newpartner'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)