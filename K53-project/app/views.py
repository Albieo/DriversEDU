from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'app/home.html'
    extra_context = { 'today': datetime.today() }

class LoginView(TemplateView):
    template_name = 'app/login.html'


