from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        labels = {
            'username': 'Käyttäjätunnus',
            'email': 'Sähköposti',
            'password1': 'Salasana',
            'password2': 'Vahvista salasana'
        }
