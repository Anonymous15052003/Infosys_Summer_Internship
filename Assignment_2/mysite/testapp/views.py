from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employees

# Create your views here.
def index(request):
    emp_list = Employees.objects.all().count()
    return HttpResponse(emp_list)