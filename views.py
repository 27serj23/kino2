from datetime import date
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm


# Create your views here.
film = Film.objects.create(title='Фильм 1', genre='Драма', director='Режиссер 1', release_date=date(2020, 1, 1))


def create_film():
    Film.objects.create(title='Фильм 2', genre='Комедия', director='Режиссер 2', release_date=date(2019, 3, 15))


def films_list(request):
    films = Film.objects.all()
    return render(request, 'films_list.html', {'films': films})


def add_film(request):
    if request.method == 'POST':
        title = request.POST['title']
        genre = request.POST['genre']
        director = request.POST['director']
        release_date = request.POST['release_date']
        Film.objects.create(title=title, genre=genre, director=director, release_date=release_date)
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FilmForm()

    films = Film.objects.all()

    return render(request, 'add_film.html', {'form': form, 'films': films})




