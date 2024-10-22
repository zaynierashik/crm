from django.urls import path
from crm_app import views

urlpatterns = [
    path('', views.login, name='login'),
    
    # Admin/Staff
    path('dashboard/', views.dashboard, name='dashboard'),
    path('company/', views.company, name='company'),
    path('contract/', views.contract, name='contract'),
    path('task/', views.task, name='task'),
    path('staff/', views.staff, name='staff'),
    path('transaction/', views.transaction, name='transaction'),
    path('sector/', views.sector, name='sector'),
    path('service/', views.service, name='service'),
    path('brand/', views.brand, name='brand'),

    path('company-details/<int:company_id>/', views.companydetails, name='companydetails'),
    path('contract-details/<int:company_id>/<int:requirement_id>/', views.contractdetails, name='contractdetails'),
    path('task-details/<int:task_id>/', views.taskdetails, name='taskdetails'),

    path('add-new-company/', views.add_newcompany, name='add_newcompany'),
    path('add-new-requirement/', views.add_newrequirement, name='add_newrequirement'),
    path('add-new-staff/', views.add_newstaff, name='add_newstaff'),
    path('add-new-transaction/', views.add_newtransaction, name='add_newtransaction'),
    path('add-new-sector/', views.add_newsector, name='add_newsector'),
    path('add-new-service/', views.add_newservice, name='add_newservice'),
    path('add-new-brand/', views.add_newbrand, name='add_newbrand'),

    path('add-transaction/<int:company_id>/<int:requirement_id>/', views.add_transaction, name='add_transaction'),
    path('assign-task/', views.assign_newtask, name='assign_newtask'),

    path('edit-company/<int:company_id>/', views.companyeditform, name='companyeditform'),
    path('edit-requirement/<int:requirement_id>/', views.requirementeditform, name='requirementeditform'),

    path('update-company/<int:company_id>', views.update_company, name='update_company'),
    path('update-requirement/<int:requirement_id>', views.update_requirement, name='update_requirement'),
    path('task/<int:task_id>/update_status/', views.update_task_status, name='update_task_status'),
    path('update-sector/', views.update_sector, name='update_sector'),
    path('update-service/', views.update_service, name='update_service'),
    path('update-brand/', views.update_brand, name='update_brand'),

    path('handle-decision/', views.handle_decision, name='handle_decision'),


    # User
    path('user/', views.user, name='user'),
    path('add-new-user/', views.add_newuser, name='add_newuser'),
    path('user-authentication/', views.user_authentication, name='user_authentication'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('company-profile/', views.company_profile, name='company_profile'),
    path('requirement/', views.requirement, name='requirement'),
    path('contact/', views.contact, name='contact'),

    path('requirement-details/<int:company_id>/<int:requirement_id>/', views.requirementdetails, name='requirementdetails'),

    path('add-company-profile/', views.add_companyprofile, name='add_companyprofile'),
    path('add-new-request/', views.add_newrequest, name='add_newrequest'),
    path('add-new-contact/', views.add_newcontact, name='add_newcontact'),

    path('update-request/', views.update_request, name='update_request'),
    path('update-contact/', views.update_contact, name='update_contact'),

    path('delete-request/<int:id>/', views.delete_request, name='delete_request'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),

    path('get-contacts/', views.get_contacts, name='get_contacts'),
    path('get-requirements/', views.get_requirements, name='get_requirements'),

    path('login-authentication/', views.login_authentication, name='login_authentication'),
    path('logout/', views.logout, name='logout'),

    path('toggle-staff-status/<int:staff_id>/', views.toggle_staff_status, name='toggle_staff_status'),
    path('export-excel/<int:company_id>/', views.export_excel, name='export_excel'),

    # path('send-email/', views.send_email, name='send_email'),
    path('predict-revenue/', views.predict_revenue, name='predict_revenue'),

    # AJAX
    path('add-sector/', views.add_sector, name='add_sector'),
]