from django.db import models
from django.utils.timezone import now

class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    resetcode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=100, default='User')
    status = models.BooleanField(default=True)
    resetcode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Sector(models.Model):
    sector_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.sector_name

class Service(models.Model):
    service_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.service_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.product_name

class Requirement(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company_requirements')
    date = models.DateField(default=now)
    contact_name = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_requirements')
    requirement_type = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True, related_name='brand_requirements')
    product_name = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='product_requirements')
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True, related_name='service_requirements')
    requirement_description = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0.00)
    status = models.CharField(max_length=100)
    progress = models.CharField(max_length=100, default='Initiated')

    def __str__(self):
        return self.requirement_type
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='tasks')
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} assigned to {self.assigned_to.full_name}"

class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True, related_name='sector_companies')
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    via = models.CharField(max_length=100, null=True, blank=True)
    referral_name = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    connection = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_companies')
    date = models.DateField(default=now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "companies"

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_contacts')
    contact_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.contact_name

class Minute(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_transactions')
    requirement = models.ForeignKey(Requirement, on_delete=models.SET_NULL, null=True, blank=True, related_name='requirement_transactions')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_transactions')
    action = models.TextField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Minute for {self.company} on {self.date}"