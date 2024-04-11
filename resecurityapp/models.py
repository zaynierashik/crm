from django.db import models
from django.contrib.auth.models import User

class Sector(models.Model):
    Sector_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Sector_Name

class Requirement(models.Model):
    Requirement_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Requirement_Name

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

class Partner(models.Model):
    Partner_Name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    Contact_Person = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.Partner_Name

class Company(models.Model):
    Company_Name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    Contact_Person = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    Phone_Number = models.CharField(max_length=20)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    Requirement_Description = models.TextField()
    price = models.CharField(max_length=100)
    via = models.ForeignKey(Via, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.Company_Name
    
    class Meta:
        verbose_name_plural = "companies"

class Transaction(models.Model):
    date = models.DateField()
    Company_Name = models.CharField(max_length=100)
    action = models.TextField()

    def __str__(self):
        return self.Company_Name