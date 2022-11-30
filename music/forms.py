from django import forms
from .models import Music, Album

class Music_Form(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'albums', 'image', 'audio_file', 'genre']

class Album_Form(forms.ModelForm):
    class Meta:
        model = Album
        fields=['title', 'Author', 'image', 'description', 'musics']