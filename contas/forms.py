from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _
from django import forms
from .models import User
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Endereço de e-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError(_('Já existe um usuário com esse nome...'))
        return username


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A duas senhas não combinam')
        return password2


    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = [
        	'first_name',
        	'last_name',
        	'username',
        	'email',
            'curso'
    	]


class EditConta(forms.ModelForm):
    first_name = forms.CharField()
    email = forms.EmailField(
        required=True,
        label='Endereço de e-mail',
        error_messages={
            'invalid': 'Insira um e-mail válido...'
        }

    )

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError(_('Já existe um usuário com esse E-mail'))
        return email


    def clean_username(self):
        username = self.cleaned_data['username']
        queryset = User.objects.filter(username=username).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError(_('Já existe alguém com esse nome de usuário'))
        return username


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]