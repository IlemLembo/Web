from django.db import models
from authentication.models import *
import mutagen


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=60)
    Author = models.ForeignKey(Profile, on_delete= models.SET_NULL, related_name='created_by', null=True)
    image = models.ImageField(verbose_name='Illustration')
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    musics = models.ForeignKey('Music', on_delete=models.SET_NULL, related_name='musics', null=True)

    def __str__(self):
        return str(self.title)


class Music(models.Model):
    RNB = 'RNB'
    GOSPEL = 'GOSPEL'
    RAP = 'RAP'
    TRADITIONAL = 'TRADITIONAL'
    LOVE = 'LOVE'
    NOSTALGIA = 'NOSTALGIA'

    GENRE_CHOICES = (
        (RNB, 'RNB'),
        (GOSPEL, 'Gospel'),
        (RAP, 'RAP'),
        (TRADITIONAL, 'Musique Traditonnel'),
        (LOVE, 'Amour'),
        (NOSTALGIA, 'Nostalgie')
    )

    title = models.TextField(verbose_name='titre', unique=True, max_length=60)
    creator = models.ForeignKey(Profile, null=True, related_name="Chanteur", blank=True, on_delete=models.SET_NULL)
    albums = models.ForeignKey(to=Album, on_delete=models.SET_NULL, related_name='album', null=True)
    image= models.ImageField(verbose_name='Illustration')
    audio_file = models.FileField(upload_to='media/', blank=False, verbose_name='fichier audio')
    genre = models.CharField(max_length=40,choices=GENRE_CHOICES, verbose_name='Genre_musical')
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ManyToManyField(Profile)

    

    def __str__(self):
        return str(self.title)

'''    @property
    def length(self):
        temp = open(self.audio_file
        , 'w')
        audio_info = mutagen.File(temp.read()).info
        length_in_sec = int(audio_info.length)
        min = int(length_in_sec // 60)
        sec = int(length_in_sec % 60)

        return (audio_info, f'{min}min {sec}sec')'''


