from datetime import datetime
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import CreateUserForm, AnswerForm
from .models import Question


class HomeView(TemplateView):
	template_name = "app/home.html"
	extra_context = {"today": datetime.today()}


class LoginInterfaceView(LoginView):
	template_name = 'app/login.html'
	success_url = '/'


class UserCreateView(FormView):
	form_class = CreateUserForm
	template_name = 'app/signup.html'
	success_url = 'app/roles_selection.html'

	def form_valid(self, form):
		form.save()
		
		return super().form_valid(form)


class QuestionDetailView(FormView):
	form_class = AnswerForm
	template_name = 'app/question_detail.html'

	def get_form_kwargs(self, *args, **kwargs):
		kwargs = super().get_form_kwargs()
		question = get_object_or_404(Question, id=self.kwargs['question_id'])
		kwargs['question'] = question

		return kwargs

	def form_valid(self, form):
		question = get_object_or_404(Question, id=self.kwargs['question_id'])
		answer = form.save(commit=False)
		answer.user = self.request.user
		answer.question = question
		answer.save()

		return super().form_valid(form)

	# def get_success_url(self):
	# 	return reverse(next_question or result)
