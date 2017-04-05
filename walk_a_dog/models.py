from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render, reverse


VOIVODESHIP = (
    (0, "wybierz województwo"),
    (1, "woj. dolnośląskie"),
    (2, "woj. kujawsko-pomorskie"),
    (3, "woj. lubelskie"),
    (4, "woj. lubuskie"),
    (5, "woj. łódzkie"),
    (6, "woj. małopolskie"),
    (7, "woj. mazowieckie"),
    (8, "woj. opolskie"),
    (9, "woj. podkarpackie"),
    (10, "woj. podlaskie"),
    (11, "woj. pomorskie"),
    (12, "woj. śląskie"),
    (13, "woj. świętokrzyskie"),
    (14, "woj. warmińsko-mazurskie"),
    (15, "woj. wielkopolskie"),
    (16, "woj. zachodniopomorskie")
)

GENDER = (
    (1, "male"),
    (2, "female")
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    voivodeship = models.IntegerField(choices=VOIVODESHIP, default=0)
    city = models.CharField(max_length=64, blank=True)
    fav_walking_place = models.TextField(blank=True)

    def __str__(self):
        return "{} | {} | {}".format(self.user, self.city, self.fav_walking_place)

    class Meta:
        verbose_name = 'Profil użytkownika'
        verbose_name_plural = 'Profile użytkowników'

    def get_absolute_url(self):
        return reverse('profile-details', kwargs={'id': self.id})

class Dog(models.Model):
    avatar = models.ImageField(upload_to='/static/', blank=True, null=True, verbose_name='Zdjęcie')
    name = models.CharField(max_length=64, verbose_name='Imię')
    gender = models.IntegerField(choices=GENDER, verbose_name='Płeć')
    year_of_birth = models.IntegerField(verbose_name='Rok urodzenia')
    breed = models.CharField(max_length=64, verbose_name='rasa')
    description = models.TextField(blank=True, null=True, verbose_name='Opis')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {} | {} | {}".format(self.name, self.gender, self.year_of_birth, self.breed)

    class Meta:
        verbose_name = 'Pies'
        verbose_name_plural = 'Psy'

class Walk(models.Model):
    voivodeship = models.IntegerField(choices=VOIVODESHIP, verbose_name='Województwo')
    city = models.CharField(max_length=64, verbose_name='Miasto')
    date_start = models.DateTimeField(verbose_name='Początek spaceru')
    date_stop = models.DateTimeField(verbose_name='Koniec spaceru')
    dog = models.ManyToManyField(Dog)

    def __str__(self):
        return "{} | {} | {} | {}".format(self.voivodeship, self.city, self.dog)

    class Meta:
        verbose_name = 'Spacer'
        verbose_name_plural = 'Spacery'









    #
    #
    #
    #
    # first_name = models.CharField(max_length=64)
    # last_name =  models.CharField(max_length=64)
    # nick_name = models.CharField(max_length=64)
    # email = models.EmailField(max_length = 254)
    #
    #
    # def __str__(self):
    #     return self.name
    #
    # @property
    # def name(self):
    #     return "{} {}".format(self.last_name, self.first_name)
    #
    # def get_absolute_url(self):
    #     return reverse('student', kwargs={'student_id': self.id}) #id studenta, więc self









