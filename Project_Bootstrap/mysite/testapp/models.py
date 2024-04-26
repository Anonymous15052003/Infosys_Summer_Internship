from django.db import models

# Create your models here.

class UserInfo1(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    mail=models.EmailField()
    address=models.CharField(max_length=200)
    phoneno=models.IntegerField()
