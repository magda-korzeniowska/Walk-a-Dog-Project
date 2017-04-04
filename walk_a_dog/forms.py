from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from walk_a_dog.models import UserProfile

class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def clean(self):
        cleaned_data = super().clean()
        raw_password = cleaned_data['password']
        cleaned_data['password'] = make_password(raw_password)
        return cleaned_data


class AuthForm(forms.Form):
    username = forms.CharField(label="Nazwa użytkownika")
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        #do views
        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Błędna nazwa użytkownika lub hasło")


        cleaned_data['user'] = user
        return cleaned_data


