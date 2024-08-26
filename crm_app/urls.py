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

    path('user/', views.user, name='user'),
    path('add-new-user/', views.add_newuser, name='add_newuser'),
    path('user-authentication/', views.user_authentication, name='user_authentication'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('company-profile/', views.company_profile, name='company_profile'),

    path('add-company-profile/', views.add_companyprofile, name='add_companyprofile'),
    path('add-new-request/', views.add_newrequest, name='add_newrequest'),

    # path('add-new-company/', views.add_newcompany, name='add_newcompany'),
    path('add-new-requirement/', views.add_newrequirement, name='add_newrequirement'),
    path('add-new-partner/', views.add_newpartner, name='add_newpartner'),
    path('add-new-staff/', views.add_newstaff, name='add_newstaff'),
    path('add-new-transaction/', views.add_newtransaction, name='add_newtransaction'),
    path('add-new-sector/', views.add_newsector, name='add_newsector'),
    path('add-new-service/', views.add_newservice, name='add_newservice'),
    path('add-new-brand/', views.add_newbrand, name='add_newbrand'),

    path('add-transaction/<int:company_id>/<int:requirement_id>/', views.add_transaction, name='add_transaction'),

    path('update-company/<int:company_id>', views.update_company, name='update_company'),
    path('update-partner/<int:partner_id>', views.update_partner, name='update_partner'),
    path('update-sector/', views.update_sector, name='update_sector'),
    path('update-service/', views.update_service, name='update_service'),
    path('update-brand/', views.update_brand, name='update_brand'),

    path('get-contacts/', views.get_contacts, name='get_contacts'),
    path('get-requirements/', views.get_requirements, name='get_requirements'),

    path('login-authentication/', views.login_authentication, name='login_authentication'),
    path('logout/', views.logout, name='logout'),

    path('toggle-staff-status/<int:staff_id>/', views.toggle_staff_status, name='toggle_staff_status'),
    path('export-excel/<int:company_id>/', views.export_excel, name='export_excel'),

    path('edit-company/<int:company_id>/', views.companyeditform, name='companyeditform'),
    path('edit-partner/<int:partner_id>/', views.partnereditform, name='partnereditform'),

    path('company-details/<int:company_id>/', views.companydetails, name='companydetails'),
    path('requirement-details/<int:company_id>/<int:requirement_id>/', views.requirementdetails, name='requirementdetails'),
    path('partner-details/<int:partner_id>/', views.partnerdetails, name='partnerdetails'),

    # path('send-email/', views.send_email, name='send_email'),
    path('predict-revenue/', views.predict_revenue, name='predict_revenue'),
]