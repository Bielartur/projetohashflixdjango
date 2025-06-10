from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from filme.models import Usuario

class FormHomepage(forms.Form):
    email = forms.EmailField(label='')

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class EditarPerfilForm(UserChangeForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='Email')

    class Meta(UserChangeForm):
        model = Usuario
        fields = ('first_name', 'last_name', 'email')

