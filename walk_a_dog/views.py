from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

from walk_a_dog.forms import AuthForm, RegisterProfileForm, AddDetailsForm
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


# class ProfileView(View):
#     def get(self, request, id):
#         profile = UserProfile.objects.get(pk=id)
#         ctx = {'profile': profile}
#         return render(request, 'walk_a_dog/profile.html', ctx)

class ProfileView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        ctx = {'profile': user}
        return render(request, 'walk_a_dog/profile.html', ctx)




class AddDetailsView(View):
    def get(self,request):
        ctx = {'form': AddDetailsForm()}
        return render(request, 'walk_a_dog/add_details.html', ctx)

    def post(self, request):
        form = AddDetailsForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            voivodeship = form.cleaned_data['voivodeship']
            city = form.cleaned_data['city']
            fav_walking_place = form.cleaned_data['fav_walking_price']

            profile_details = UserProfile.objects.create(
                voivodeship=voivodeship,
                city=city,
                fav_walking_place=fav_walking_place
            )
            return HttpResponseRedirect(profile_details.get_absolute_url())

        return render(request, "walk_a_dog/add_details.html", ctx)

