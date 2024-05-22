from django.contrib import admin
from .models import Company, Sector, Service, Via, Status, Brand, Partner, Transaction

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('Company_Name', 'sector', 'Contact_Person', 'email', 'Phone_Number', 'service', 'brand', 'price')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('Partner_Name', 'Contact_Person', 'email')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Company_Name', 'date', 'action', 'remark')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Sector)
admin.site.register(Service)
admin.site.register(Via)
admin.site.register(Status)
admin.site.register(Brand)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Transaction, TransactionAdmin)