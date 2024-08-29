from django import forms
from .models import User, Role


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'confirm_password', 'licence_type', 'licence_code']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'password': 'Password',
            'confirm_password': 'Confirm Password',
            'licence_type': 'Licence Type',
            'licence_code': 'Licence Code'
        }

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password

    licence_type = forms.ChoiceField(choices=Role.LICENCE_TYPE_CHOICES, label='', widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),)
    licence_code = forms.ChoiceField(choices=Role.LICENCE_CODE_CHOICES, label='Licence Code', widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['licence_type'].label = 'Licence Type'
        self.fields['licence_code'].label = 'Licence Code'
