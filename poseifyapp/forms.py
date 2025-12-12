from django import forms
from .models import ModelProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = ModelProfile
        fields = '__all__'
