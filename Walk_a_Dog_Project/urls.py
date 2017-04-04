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

from walk_a_dog.views import IndexView, LoginView, LogoutView, RegisterProfileView, ProfileView, AddDetailsView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^walkadog$', IndexView.as_view(), name="index"),
    url(r'^walkadog/login$', LoginView.as_view(), name='login'),
    url(r'^walkadog/logout$', LogoutView.as_view(), name='logout'),
    url(r'^walkadog/register$', RegisterProfileView.as_view(), name='register'),
    url(r'^walkadog/profile/(?P<id>(\d)+)$', ProfileView.as_view(), name='profile'),
    url(r'^walkadog/add_details$', AddDetailsView.as_view(), name='add-details'),

    # url(r'^category/(?P<slug>[-\w]+)', CategoryView.as_view(), name="category"),
    # # !!!!! slug tu wchodzi dziwny więc -\w
    # url(r'^product/(?P<product_id>(\d)+)', ProductView.as_view(), name="product"),
    # # url(r'^products/$', ProductsView.as_view(), name='products'),
]
