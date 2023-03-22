"""
All the Django forms that will be used for pets.
"""

from django import forms
from .models import Pet

class PetCreationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'