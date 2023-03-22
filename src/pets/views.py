"""
Views related to functionality about pets.
"""

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from forms import PetCreationForm

class ListPets(ListView):
    """Class that will list all the pets."""
    context_object_name = 'pets'
    template_name = 'pets/list.html'


class CreatePet(CreateView):
    """Class for adding new pets to the system."""
    template_name = 'pets/create.html'
    form_class = PetCreationForm


