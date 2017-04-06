"""Walk_a_Dog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from walk_a_dog.views import (
    IndexView,
    LoginView,
    LogoutView,
    RegisterProfileView,
    ProfileView,
    ProfileDetailedView,
    AddDetailsView,
    UpdateProfileView, AddDogView, ModifyDogView, AddWalkView, ModifyWalkView, DogView, WalkView, JoinWalkView,
    UpdateUserView,
    ModifyProfileView,
    SearchWalkView,
    DeleteWalkView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^accounts/', admin.site.urls),
    url(r'^walkadog$', IndexView.as_view(), name="index"),
    url(r'^walkadog/login$', LoginView.as_view(), name='login'),
    url(r'^walkadog/logout$', LogoutView.as_view(), name='logout'),
    url(r'^walkadog/register$', RegisterProfileView.as_view(), name='register'),
    url(r'^walkadog/profile/(?P<id>(\d)+)$', ProfileView.as_view(), name='profile'),
    url(r'^walkadog/add_details$', AddDetailsView.as_view(), name='add-details'),
    url(r'^walkadog/profile_details/(?P<id>(\d)+)$', ProfileDetailedView.as_view(), name='profile-details'),
    url(r'^walkadog/update_user/(?P<pk>(\d+))$', UpdateUserView.as_view(), name='update-user'),
    url(r'^walkadog/update_profile/(?P<pk>(\d+))$', UpdateProfileView.as_view(), name='update-profile'),
    url(r'^walkadog/modify_profile/', ModifyProfileView.as_view(), name='modify-profile'),
    url(r'^walkadog/add_dog$', AddDogView.as_view(), name='add-dog'),
    # url(r'^walkadog/dog_added$', AddDogView.as_view(), name='dog-added'),
    url(r'^walkadog/modify_dog/(?P<pk>(\d+))', ModifyDogView.as_view(), name='modify-dog'),
    url(r'^walkadog/dog_details/(?P<id>(\d+))', DogView.as_view(), name='dog_details'),
    url(r'^walkadog/walks$', WalkView.as_view(), name='walks'),
    url(r'^walkadog/add_walk$', AddWalkView.as_view(), name='add-walk'),
    url(r'^walkadog/join_walk/(?P<walk_id>(\d+))$', JoinWalkView.as_view(), name='join-walk'),
    url(r'^walkadog/modify_walk/(?P<pk>(\d+))', ModifyWalkView.as_view(), name='modify-walk'),
    url(r'^walkadog/search_walk/', SearchWalkView.as_view(), name='search-walk'),
    url(r'^walkadog/delete_walk/', DeleteWalkView.as_view(), name='delete-walk'),
]
