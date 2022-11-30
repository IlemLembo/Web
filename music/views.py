from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Music_Form
from . import models

# Create your views here.
@login_required
def dashboard(request):
    audio = models.Music.objects.all()
    return render(request, 'dashboard.html', context={
        'audio' : audio,
    })

def Audio_Upload(request):
    form = Music_Form()
    if request.method == 'POST':
        form = Music_Form(request.POST, request.FILES)
        if form.is_valid():
            # Gardes moi ça au chaud ne sauvegarde pas encore dans ma base de donnée:
            audio = form.save(commit=False)
            # Spécifions le créateur du fichier:
            audio.creator = request.user
            # Maintenant tu peux sauvegarder 👌
            audio.save()
            return redirect('home')
    return render(request, 'publicate.html', context={
        'form' : form,
    })