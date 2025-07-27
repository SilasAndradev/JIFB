from django.forms import ModelForm
from base.models import Perfil
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditarUserProfileForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'foto_de_perfil']
        exclude = ['user']
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_de_perfil': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto_de_perfil'].required = False

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        labels = {
            'username': 'Nome de usuário',
            'email': 'Endereço de e-mail',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'