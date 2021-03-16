from django.db import models

from user_company_db.models import UserCompany


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    company = models.ForeignKey(UserCompany, on_delete=models.CASCADE, related_name='employee')
