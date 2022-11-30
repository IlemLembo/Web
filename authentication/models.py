from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLES_CHOICES = (
        (CREATOR, "Créateur"),
        (SUBSCRIBER, "Abonné"),
    )

    profile_photo = models.ImageField(verbose_name='Photo de Profil')
    role = models.CharField(max_length=30, choices=ROLES_CHOICES, verbose_name='Rôle')
    email = models.EmailField(verbose_name='email', name='email')

class Profile(models.Model):
    HOMME = 'Homme'
    FEMME = 'Femme'
    GENDER_CHOICES = (
        (HOMME, 'homme'),
        (FEMME, 'femme'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    bio = models.TextField()
    phone = models.CharField(max_length=30 ,verbose_name = 'Numero de Telephone')
    def __str__(self):
        return str(self.user)






'''
class Music(models.Model):
    likes = models.ManyToManyField(User, related_name='likes')
    def __str__(self):
        return self.likes.count()'''