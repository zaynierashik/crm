from django.contrib import admin
from .models import Staff, Company, Requirement, Sector, Service, Brand, Product, Partner, Contact, Transaction

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'Company_Name')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'Full_Name', 'email', 'role')

class RequirementAdmin(admin.ModelAdmin):
    list_display = ('id', 'Requirement_Type', 'company', 'Contact_Name', 'brand', 'Product_Name', 'service')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Contact_Name', 'company', 'designation')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Partner_Name', 'Contact_Person', 'email')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'company')

admin.site.register(Staff, StaffAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Sector)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Transaction, TransactionAdmin)