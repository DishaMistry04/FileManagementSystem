from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Users(User):
    contact = models.BigIntegerField()

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.email


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm_password')

    class Meta:
        model = Users
        fields = ['first_name','last_name','email','contact','password']

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
