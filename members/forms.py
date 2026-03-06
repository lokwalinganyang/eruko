from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class MemberRegistrationForm(UserCreationForm):
    national_id = forms.CharField(required=True, help_text="Enter your ID Number")
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('national_id', 'phone_number')