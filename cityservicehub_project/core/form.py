# core/form.py
from django import forms
from .models import Users,Services,ServiceProvider

class UsersForm(forms.ModelForm):
    conform = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter confirm password",
            }
        )
    )
    class Meta:
        model = Users
        fields = ["name", "email", "phone", "password", "adress", "status", "gender","photo"]
        labels = {
            "password": "Password",
            "photo":"Profile picture",
            "name": "Full Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "adress": "Address",
            "status": "Status",
            "reference": "Gender",
        }
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
            "conform": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Conform password"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter phone number"}),
            "adress": forms.Textarea(attrs={"class": "form-control", "rows": 1, "placeholder": "Enter address"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "gender": forms.RadioSelect(attrs={"class": "form-check-input"}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }
      

class ServicesForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=["service_name","providers"]
        widgets={
            "service_name":forms.Textarea(attrs={"class": "form-control", "rows": 1, "placeholder": "Enter Service name"}),
            "providers":forms.SelectMultiple(attrs={"class":"form-select","multiple":"multiple"})
        }

class LoginForm(forms.Form):
   
   email = forms.EmailField(
        label="Enter Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )
   password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password"
        }))
   