from django.db import models
from django.contrib.auth.models import User

class Sector(models.Model):
    Sector_Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Sector_Name

class Service(models.Model):
    Service_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Service_Name

class Status(models.Model):
    Status_Name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "status"
    
    def __str__(self):
        return self.Status_Name

class Via(models.Model):
    Via_Name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "via"
        verbose_name_plural = "via"

    def __str__(self):
        return self.Via_Name
    
class Brand(models.Model):
    Brand_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Brand_Name

class Partner(models.Model):
    Partner_Name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    Contact_Person = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.Partner_Name

class Company(models.Model):
    Company_Name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)
    Contact_Person = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    Phone_Number = models.CharField(max_length=20)
    requirement = models.CharField(max_length=100, default=None)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    Product_Name = models.CharField(max_length=100, null=True)
    Requirement_Description = models.TextField()
    currency = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    via = models.ForeignKey(Via, on_delete=models.SET_NULL, null=True)
    Referral_Name = models.CharField(max_length=100, null=True)
    Partner_Name = models.CharField(max_length=100, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Company_Name
    
    class Meta:
        verbose_name_plural = "companies"

class Transaction(models.Model):
    date = models.DateField()
    Company_Name = models.CharField(max_length=100)
    action = models.TextField()
    remark = models.TextField()

    def __str__(self):
        return self.Company_Name