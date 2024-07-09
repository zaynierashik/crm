from django.contrib import admin
from .models import Staff, Company, Requirement, Sector, Service, Brand, Partner, Contact, Transaction

class StaffAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'email', 'role')

class RequirementAdmin(admin.ModelAdmin):
    list_display = ('Requirement_Type', 'company', 'Contact_Name', 'brand', 'Product_Name', 'service')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Contact_Name', 'company', 'designation')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('Partner_Name', 'Contact_Person', 'email')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('company', 'brand', 'Product_Name', 'service')

admin.site.register(Staff, StaffAdmin)
admin.site.register(Company)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Sector)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Transaction, TransactionAdmin)