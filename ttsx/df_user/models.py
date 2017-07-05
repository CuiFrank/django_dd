from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=20)
