from datetime import datetime
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView

from .forms import CreateUserForm, AnswerForm, LoginForm
from .models import Question


class HomeView(TemplateView):
	template_name = "app/home.html"
	extra_context = {"today": datetime.today()}


class UserCreateView(CreateView):
	form_class = CreateUserForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		
		return super().form_valid(form)
	

class LoginInterfaceView(LoginView):
	form_class = LoginForm
	template_name = 'registration/login.html'


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
