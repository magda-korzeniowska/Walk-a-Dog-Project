from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

from walk_a_dog.forms import AuthForm, RegisterProfileForm
from walk_a_dog.models import UserProfile


class IndexView(View):

    def get(self, request):
        return render(request, 'walk_a_dog/index.html', {})

class RegisterProfileView(View):

    def get(self, request):
        form = RegisterProfileForm()
        ctx = {'form': form}
        return render(request, 'walk_a_dog/register_profile_form.html', ctx)

    def post(self, request):
        form = RegisterProfileForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.create(user=user) #rozszerzenie o extended user
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'walk_a_dog/register_profile_form.html', ctx)


class LoginView(View):
    def get(self,request):
        ctx = {'form': AuthForm()}
        return render(request, 'walk_a_dog/login.html', ctx)

    def post(self,request):
        form = AuthForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'walk_a_dog/login.html', ctx)


class LogoutView(View):
    def get (self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


