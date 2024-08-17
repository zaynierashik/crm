from django.urls import path
from crm_app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('setting/', views.setting, name='setting'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('company/', views.company, name='company'),
    path('requirement/', views.requirement, name='requirement'),
    path('partner/', views.partner, name='partner'),
    path('staff/', views.staff, name='staff'),
    path('transaction/', views.transaction, name='transaction'),
    path('sector/', views.sector, name='sector'),
    path('service/', views.service, name='service'),
    path('brand/', views.brand, name='brand'),

    path('add-new-company/', views.add_newcompany, name='add_newcompany'),
    path('add-new-partner/', views.add_newpartner, name='add_newpartner'),
    path('add-new-staff/', views.add_newstaff, name='add_newstaff'),
    path('add-new-sector/', views.add_newsector, name='add_newsector'),
    path('add-new-service/', views.add_newservice, name='add_newservice'),
    path('add-new-brand/', views.add_newbrand, name='add_newbrand'),

    path('login-authentication/', views.login_authentication, name='login_authentication'),
    path('logout/', views.logout, name='logout'),

    path('toggle-staff-status/<int:staff_id>/', views.toggle_staff_status, name='toggle_staff_status'),
    path('export-excel/<int:company_id>/', views.export_excel, name='export_excel'),

    path('company-details/<int:company_id>/', views.companydetails, name='companydetails'),
    path('requirement-details/<int:company_id>/<int:requirement_id>/', views.requirementdetails, name='requirementdetails'),
]