from django.db import models
from django.contrib.auth.models import User

class Sector(models.Model):
    sector_name = models.CharField(max_length=100)

class Requirement(models.Model):
    requirement_name = models.CharField(max_length=100)

class Status(models.Model):
    status_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "status"

class Via(models.Model):
    via_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "via"
        verbose_name_plural = "via"

class Partner(models.Model):
    partner_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    requirement_description = models.TextField()
    via = models.ForeignKey(Via, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "companies"
