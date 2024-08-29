from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import User
from .forms import UserForm


class HomeView(TemplateView):
    template_name = 'app/home.html'
    extra_context = { 'today': datetime.today() }


class LoginInterfaceView(LoginView):
    template_name = 'app/login.html'


class UserCreateView(CreateView):
	model = User
	form_class = UserForm
	template_name = 'app/signup.html'
	success_url = 'app/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create User'

		return context
