from django.db import models

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Dept_name = models.CharField(max_length=20)
    joining_date = models.DateField()
    salary = models.IntegerField()