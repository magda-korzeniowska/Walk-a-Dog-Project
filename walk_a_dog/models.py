from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


VOIVODESHIP = (
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
    user = models.OneToOneField(User, null=True, default=None)
    voivodeship = models.IntegerField(choices=VOIVODESHIP)
    city = models.CharField(max_length=64)
    fav_walking_place = models.TextField()

    def __str__(self):
        return "{} | {} | {}".format(self.user, self.city, self.fav_walking_place)

    class Meta:
        verbose_name = 'Profil użytkownika'
        verbose_name_plural = 'Profile użytkowników'

class Dog(models.Model):
    avatar = models.ImageField(upload_to='/static/')
    name = models.CharField(max_length=64)
    gender = models.IntegerField(choices=GENDER)
    year_of_birth = models.IntegerField()
    breed = models.CharField(max_length=64)
    description = models.TextField(null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {} | {} | {}".format(self.name, self.gender, self.year_of_birth, self.breed)

    class Meta:
        verbose_name = 'Pies'
        verbose_name_plural = 'Psy'

class Walk(models.Model):
    voivodeship = models.IntegerField(choices=VOIVODESHIP)
    city = models.CharField(max_length=64)
    date_start = models.DateTimeField()
    date_stop = models.DateTimeField()
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









