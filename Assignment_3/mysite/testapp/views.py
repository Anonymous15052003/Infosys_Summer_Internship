from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserInfoForm1
from django.urls import reverse
from testapp.models import UserInfo1

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