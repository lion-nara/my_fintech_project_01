from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not re.match(r'^[A-Za-z0-9]+$', username):
            raise forms.ValidationError("아이디는 영어와 숫자만 사용할 수 있습니다.")
        return username

    def clean_password1(self):
        pw = self.cleaned_data.get("password1")
        if len(pw) < 4:
            raise forms.ValidationError("비밀번호는 최소 4자리 이상이어야 합니다.")
        return pw
