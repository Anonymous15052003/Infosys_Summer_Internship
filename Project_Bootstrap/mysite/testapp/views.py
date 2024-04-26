from django.shortcuts import render
from .forms import UserInfoForm1
from testapp.models import UserInfo1
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def success(request):
    return render(request,'success.html')

def submit_form(request):
    if request.method == 'POST':
        form = UserInfoForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success.html')
# Redirect to a success page
    else:
        form = UserInfoForm1()
    return render(request, 'register.html', {'form': form})



def index(request):
    emp_list = UserInfo1.objects.all().count()
    return HttpResponse(emp_list)


def register(request):
    return render(request,'index.html')


def menu(request):
    return render(request,'Menu.html')

def feed(request):
    return render(request,'FeedBack.html')


def product(request):
    return render(request,'product.html')

def login(request):
    return render(request,'login.html')




