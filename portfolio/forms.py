# portfolio/forms.py
from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name","type","currency"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "type": forms.Select(attrs={"class":"form-select"}),
            "currency": forms.TextInput(attrs={"class":"form-control"}),
        }

