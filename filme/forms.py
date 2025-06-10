from django.contrib.auth.forms import UserCreationForm
from django import forms

from filme.models import Usuario

class FormHomepage(forms.Form):
    email = forms.EmailField(label='')

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

