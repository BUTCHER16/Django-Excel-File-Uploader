from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        