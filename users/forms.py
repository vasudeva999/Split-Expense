from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN'),
        # widget=forms.TextInput(attrs={'placeholder': ('Phone')}), 
        # label=("Phone number"),
    )

    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']

