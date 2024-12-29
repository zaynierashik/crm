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
    path('product/', views.product, name='product'),
    path('brand/', views.brand, name='brand'),

    path('company-details/<int:company_id>/', views.companydetails, name='companydetails'),
    path('contract-details/<int:company_id>/<int:requirement_id>/', views.contractdetails, name='contractdetails'),
    path('task-details/<int:task_id>/', views.taskdetails, name='taskdetails'),
    path('requirementform/', views.requirementform, name='requirementform'),

    path('add-new-company/', views.add_newcompany, name='add_newcompany'),
    path('add-new-requirement/', views.add_newrequirement, name='add_newrequirement'),
    path('add-requirement/', views.add_requirement, name='add_requirement'),
    path('add-new-staff/', views.add_newstaff, name='add_newstaff'),
    path('add-new-transaction/', views.add_newtransaction, name='add_newtransaction'),
    path('add-new-sector/', views.add_newsector, name='add_newsector'),
    path('add-new-service/', views.add_newservice, name='add_newservice'),
    path('add-new-product/', views.add_newproduct, name='add_newproduct'),
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
    path('update-product/', views.update_product, name='update_product'),
    path('update-brand/', views.update_brand, name='update_brand'),

    # User
    path('requirement/', views.requirement, name='requirement'),

    path('get-contacts/', views.get_contacts, name='get_contacts'),
    path('get-requirements/', views.get_requirements, name='get_requirements'),

    path('login-authentication/', views.login_authentication, name='login_authentication'),
    path('logout/', views.logout, name='logout'),

    path('toggle-staff-status/<int:staff_id>/', views.toggle_staff_status, name='toggle_staff_status'),
    path('export-excel/<int:company_id>/', views.export_excel, name='export_excel'),

    # path('send-email/', views.send_email, name='send_email'),

    # AJAX
    path('add-sector-ajax/', views.add_sector_ajax, name='add_sector_ajax'),
    path('add-service-ajax/', views.add_service_ajax, name='add_service_ajax'),
    path('add-brand-ajax/', views.add_brand_ajax, name='add_brand_ajax'),
    path('add-product-ajax/', views.add_product_ajax, name='add_product_ajax'),

    path('get-states/', views.get_states, name='get_states'),

    #Reset Password
    path('admin_reset_password/',views.admin_reset_password, name='admin_reset_password'),
    path('admin_reset_code/',views.admin_reset_code, name='admin_reset_code'),
    path('admin_reset_passwordDone/',views.admin_reset_passwordDone, name='admin_reset_passwordDone'),
]