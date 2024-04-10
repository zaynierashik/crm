from django.contrib import admin
from .models import Company, Sector, Requirement, Via, Status, Partner

admin.site.register(Company)
admin.site.register(Sector)
admin.site.register(Requirement)
admin.site.register(Via)
admin.site.register(Status)
admin.site.register(Partner)