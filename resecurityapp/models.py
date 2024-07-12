from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    Full_Name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    role = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.Full_Name

class Sector(models.Model):
    Sector_Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Sector_Name

class Service(models.Model):
    Service_Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Service_Name
    
class Brand(models.Model):
    Brand_Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Brand_Name

class Partner(models.Model):
    Partner_Name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    Contact_Person = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.Partner_Name

class Company(models.Model):
    Company_Name = models.CharField(max_length=100, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True, related_name='companies')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    via = models.CharField(max_length=100, null=False, blank=False)
    Referral_Name = models.CharField(max_length=100, null=True, blank=True)
    Partner_Name = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True, related_name='companies')
    Created_By = models.CharField(max_length=100, null=True, blank=True, default='Staff')

    def __str__(self):
        return self.Company_Name
    
    class Meta:
        verbose_name_plural = "companies"

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contact_persons')
    Contact_Name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=20)

    def __str__(self):
        return self.Contact_Name

class Requirement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='requirements')
    Contact_Name = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    Requirement_Type = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='requirements')
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='requirements')
    Requirement_Description = models.TextField()
    currency = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.Requirement_Type

class Transaction(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='transactions')
    Requirement_Type = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    Contact_Name = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.TextField()
    remark = models.TextField()
    Created_By = models.CharField(max_length=100, null=True, blank=True, default='Staff')

    def __str__(self):
        return f"{self.company}"