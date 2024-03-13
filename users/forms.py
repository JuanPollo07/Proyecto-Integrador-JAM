from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Usuario'
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Contraseña'
        })
    class Meta:
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Usuario'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Nombre'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Apellido'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Email'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input-control',
            'placeholder': 'Confirme su contraseña'
        })
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
  