"""
Home page of the app.
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
import json
import requests


User = get_user_model()

# Create your views here.

class Homepage(TemplateView):
    template_name = 'core/homepage.html'

    def get(self, request, *args, **kwargs):
        created_users = User.objects.all()
        response = requests.get('https://3y1hl3jca0.execute-api.us-east-1.amazonaws.com/pacientes_endpoint')
        listed_users = json.loads(response.json())
        print(listed_users)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)