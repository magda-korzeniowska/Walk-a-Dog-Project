from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm, Textarea

from walk_a_dog.models import UserProfile, VOIVODESHIP, Dog, Walk


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
        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Błędna nazwa użytkownika lub hasło")
        cleaned_data['user'] = user
        return cleaned_data

class AddDetailsForm(forms.Form):
    voivodeship = forms.ChoiceField(label="województwo", choices=VOIVODESHIP)
    city = forms.CharField(label="miasto", max_length=64)
    fav_walking_place = forms.CharField(label="ulubione miejsce na spacery", widget=forms.Textarea)

class AddDogForm(ModelForm):
    class Meta:
        model = Dog
        widgets = {'description': Textarea (attrs={'cols': 80, 'rows': 10}),}
        fields = ['name', 'gender', 'avatar', 'year_of_birth', 'breed', 'description']

class AddWalkForm(ModelForm):
    class Meta:
        model = Walk
        fields = ['voivodeship', 'city', 'date_start', 'date_stop']

