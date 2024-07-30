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
    path('submit_signup/', views.submit_signup, name='submit_signup'),
    path('', views.login, name='login'),
    path('submit-login/', views.submit_login, name='submit_login'),
    path('toggle-staff-status/<int:staff_id>/', views.toggle_staff_status, name='toggle_staff_status'),
    path('logout/', views.logout, name='logout'),
    path('transaction/', views.transaction, name='transaction'),
    path('report/', views.report, name='report'),
    path('generate-report/', views.generate_report, name='generate_report'),
    path('transactiondetails/<int:company_id>/<int:requirement_id>/', views.transactiondetails, name='transactiondetails'),
    path('get-companydetails/', views.get_companydetails, name='get_companydetails'),
    path('get-contacts/', views.get_contacts, name='get_contacts'),
    path('get-requirements/', views.get_requirements, name='get_requirements'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('master/', views.master, name='master'),
    path('newform/', views.newform, name='newform'),
    path('submit-requirement/', views.submit_requirement, name='submit_requirement'),
    path('submit-transaction/', views.submit_transaction, name='submit_transaction'),
    path('transactions/<int:company_id>/<int:requirement_id>/add/', views.add_transaction, name='add_transaction'),
    path('submit-company/', views.submit_company, name='submit_company'),
    path('submit-sector/', views.submit_sector, name='submit_sector'),
    path('add-sector/', views.add_sector, name='add_sector'),
    path('submit-service/', views.submit_service, name='submit_service'),
    path('add-service/', views.add_service, name='add_service'),
    path('update-service', views.update_service, name='update_service'),
    path('submit-brand/', views.submit_brand, name='submit_brand'),
    path('add-brand/', views.add_brand, name='add_brand'),
    path('submit-product/', views.submit_product, name='submit_product'),
    path('submit-partner/', views.submit_partner, name='submit_partner'),
    path('companyform/<int:company_id>/', views.companyform, name='companyform'),
    path('companydetails/<int:company_id>/', views.companydetails, name='companydetails'),
    path('partnerform/<int:partner_id>/', views.partnerform, name='partnerform'),
    path('partnerdetails/<int:partner_id>/', views.partnerdetails, name='partnerdetails'),
    path('newcompany/', views.newcompany, name='newcompany'),
    path('submit-newcompany/', views.submit_newcompany, name='submit_newcompany'),
    path('newpartner/', views.newpartner, name='newpartner'),
    path('submit-newpartner/', views.submit_newpartner, name='submit_newpartner'),
    path('add-newpartner/', views.add_newpartner, name='add_newpartner'),
    path('export-excel/<int:company_id>/', views.export_excel, name='export_excel'),
    path('export-pdf/<int:company_id>/', views.export_pdf, name='export_pdf'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)