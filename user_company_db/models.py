from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserCompany(models.Model):
    class Meta:
        db_table = 'company'

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=300)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_company')
