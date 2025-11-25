# core/form.py
from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name", "email", "phone", "password", "adress", "status", "reference"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter phone number"}),
            "adress": forms.Textarea(attrs={"class": "form-control", "rows": 1, "placeholder": "Enter address"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "reference": forms.Select(attrs={"class": "form-select"}),
        }
