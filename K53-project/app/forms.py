from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Answer, Choice, User


class CreateUserForm(UserCreationForm):
    usable_password = None

    first_name = forms.CharField(
        label="First Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    licence_type = forms.ChoiceField(
        label="Licence Type",
        choices=(
            ("Learner", "Learners Licence Student"),
            ("Driver", "Drivers Licence Student"),
        ),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    licence_code = forms.ChoiceField(
        label="Licence Code",
        choices=(
            ("", "Licence Codes"),
            (1, "Code A"),
            (2, "Code B"),
            (3, "Code C"),
            (4, "Code E"),
        ),
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
            "licence_type",
            "licence_code",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Username..'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Password'})
    )


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['selected_choice']

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['selected_choice'].queryset = Choice.objects.filter(question=question)
        self.fields['selected_choice'].widget = forms.RadioSelect()
