from django import forms
from .models import UserInfo1

class UserInfoForm1(forms.ModelForm):
    class Meta:
        model = UserInfo1
        fields = ['name', 'age','mail', 'address','phoneno']