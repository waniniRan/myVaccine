# system_admin/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import healthfacility, Vaccination, Facilityadmin


class healthfacilityform(forms.ModelForm):
    class Meta:
        model = healthfacility
        fields = ['name', 'location', 'contact_phone', 'contact_email']


class Vaccinationform(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ['name',  'diseasePrevented', 'dose', 'description']



class FacilityAdminCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    facility = forms.ModelChoiceField(queryset=healthfacility.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'facility']