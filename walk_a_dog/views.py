from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from walk_a_dog.forms import AuthForm, RegisterProfileForm, AddDetailsForm, AddDogForm, AddWalkForm, AddWalkForm, \
SearchWalkForm
from walk_a_dog.models import UserProfile, Dog, Walk


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
            #userprofile = UserProfile.objects.create(user=user) #rozszerzenie o extended user
            login(request, user)
            return HttpResponseRedirect(reverse('add-details'))
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
        return render(request, 'walk_a_dog/userprofile_form.html', ctx)

    def post(self, request):
        form = AddDetailsForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            voivodeship = form.cleaned_data['voivodeship']
            city = form.cleaned_data['city']
            fav_walking_place = form.cleaned_data['fav_walking_place']

            userprofile = UserProfile.objects.create(
                user=request.user,
                voivodeship=voivodeship,
                city=city,
                fav_walking_place=fav_walking_place
            )
            return HttpResponseRedirect(userprofile.get_absolute_url())

        return render(request, "walk_a_dog/userprofile_form.html", ctx)


class ProfileDetailedView(View):
    def get(self, request, id):
        user = UserProfile.objects.get(pk=id)
        ctx = {'profile': user}
        return render(request, 'walk_a_dog/profile_details.html', ctx)


class UpdateUserView(UpdateView):
    template = 'walk_a_dog/register_profile_form.html'
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UpdateProfileView(UpdateView):
    template = 'walk_a_dog/userprofile_form.html'
    model = UserProfile
    fields = ['voivodeship','city','fav_walking_place']
    success_url = 'index.html'

class AddDogView(View):

    def get(self, request):
        ctx = {'form': AddDogForm()}
        return render(request, "walk_a_dog/add_dog.html", ctx)


    def post(self, request):
        form = AddDogForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            dog = form.save(commit=False)       #nie komituje się od razu, tylko czeka na cały obiekt
            dog.user = request.user
            dog.save()

            return render(request, "walk_a_dog/dog_added.html")
            # return HttpResponseRedirect(reverse('add-dog'))
        else:
            return render(request, "walk_a_dog/add_dog.html", ctx)




#------------------------------------------------------------------------------


#
# class ModifyDogView(View):
#     # permission_required = ['walk_a_dog.change_dog']
#
#     def get(self, request, id):
#         user = request.user
#         dog = Dog.objects.get(user=request.user)
#         form = AddDogForm(initial={
#             'name': dog.name,
#             'avatar': dog.avatar,
#             'gender': dog.gender,
#             'year_of_birth': dog.year_of_birth,
#             'description': dog.description,
#             'user': request.user
#         })
#         ctx = {'form': form,
#                'dog': dog}
#         return render(request, "walk_a_dog/modify_dog.html", ctx)
#
#     def post(self, request, id):
#         dog = Dog.objects.get(pk=id)
#         form = AddDogForm(data=request.POST)
#         ctx = {'form': form,
#                'dog': dog}
#
#         if form.is_valid():
#             dog.name = form.cleaned_data['name']
#             dog.avatar = form.cleaned_data['avatar']
#             dog.gender = form.cleaned_data['gender']
#             dog.year_of_birth = form.cleaned_data['year_of_birth']
#             dog.description = form.cleaned_data['description']
#             dog.user = form.cleaned_data['user']
#
#             dog.save()
#             return HttpResponseRedirect('/walkadog/modify_profile/{}').format(self.id)
#
#         return render(request, "Walk_a_dog/modify_dog.html", ctx)



class ModifyDogView(UpdateView):
    # permission_required = ['walk_a_dog.change_dog']

    template_name = 'walk_a_dog/modify_dog.html'
    model = Dog
    fields = '__all__'
    success_url = '/walkadog'



#-------------------------------------------------------------------------------




class DogView(View):
    pass
    # def get(self, request, id):
    #     User.objects.get(pk=id)
    #     dogs = Dog.objects.all()
    #     ctx = {'dogs': dogs}
    #     return render(request, 'walk_a_dog/dog_details.html', ctx)

class WalkView(View):
    def get(self, request):
        walks = Walk.objects.all()
        ctx = {'walks': walks}
        return render(request, 'walk_a_dog/walks.html', ctx)


class AddWalkView(View):

    def get(self, request):
        ctx = {'form': AddWalkForm()}
        return render(request, "walk_a_dog/add_walk.html", ctx)

    def post(self, request):
        form = AddWalkForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            walk = form.save()
            dogs = request.user.dog_set.all()
            # print(dogs)
            # print("walk", walk)
            walk.dog.add(*dogs)
            walk.save()
            return render(request, "walk_a_dog/walks.html")
        else:
            return render(request, "walk_a_dog/add_walk.html", ctx)

class ModifyWalkView(PermissionRequiredMixin, UpdateView):
    permission_required = ['walk_a_dog.change_walk']
    template_name = 'walk_a_dog/modify_walk.html'
    model = Walk
    fields = '__all__'

class JoinWalkView(View):
    def get(self, request, walk_id):
        user = request.user
        walk = Walk.objects.get(pk = walk_id)
        dogs = request.user.dog_set.all()
        walk.dog.add(*dogs)
        walk.save()
        return render(request, 'walk_a_dog/join_walk.html')


class ModifyProfileView(View):
    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=request.user) #(user=request.user)
        dogs = request.user.dog_set.all()
        ctx = {'profile': profile,
               'user': user,
               'dogs': dogs}
        return render(request, 'walk_a_dog/modify_profile.html', ctx)

class SearchWalkView(View):

    def get(self,request):
        form = SearchWalkForm()
        ctx = {'form': form}
        return render(request,'walk_a_dog/search_results.html', ctx)

    def post(self,request):
        form = SearchWalkForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            place  = form.cleaned_data['place']
            walks = Walk.objects.filter(place__icontains=place)
            ctx['results'] = walks
        return render(request, 'walk_a_dog/search_walk.html', ctx)

class DeleteWalkView(DeleteView):
    model = Walk
    success_url = '/'
