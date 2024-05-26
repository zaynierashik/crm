from django.contrib import admin
from .models import Staff, Role, Company, Sector, Service, Via, Status, Brand, Partner, ContactPerson, Transaction

class StaffAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'email', 'role')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('Company_Name', 'sector', 'service', 'brand', 'price')

class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('Contact_Name', 'company', 'designation')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('Partner_Name', 'Contact_Person', 'email')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Company_Name', 'date', 'action', 'remark')

admin.site.register(Staff, StaffAdmin)
admin.site.register(Role)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Sector)
admin.site.register(Service)
admin.site.register(Via)
admin.site.register(Status)
admin.site.register(Brand)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Transaction, TransactionAdmin)