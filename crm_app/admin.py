from django.contrib import admin
from .models import *

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role', 'status')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role', 'status')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector_name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'sector', 'city', 'country', 'status')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'company', 'designation', 'email', 'phone_number')

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('requirement_type', 'company', 'price', 'brand', 'product_name', 'service', 'progress')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'due_date', 'status')

@admin.register(Minute)
class MinuteAdmin(admin.ModelAdmin):
    list_display = ('date', 'company', 'requirement', 'contact', 'action', 'remark')