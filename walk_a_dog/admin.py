from django.contrib import admin
from django.contrib.auth.models import User

from walk_a_dog.models import UserProfile, Dog, Walk

admin.site.register(UserProfile)
admin.site.register(Dog)
admin.site.register(Walk)
