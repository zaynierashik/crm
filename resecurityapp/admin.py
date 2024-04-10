from django.contrib import admin
from .models import Company, Sector, Requirement, Via, Status, Partner

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('Company_Name', 'sector', 'Contact_Person', 'email', 'Phone_Number', 'requirement', 'price')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('Partner_Name', 'Contact_Person', 'email')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Sector)
admin.site.register(Requirement)
admin.site.register(Via)
admin.site.register(Status)