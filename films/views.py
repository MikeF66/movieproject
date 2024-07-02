from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm

def index(request):
    all_films = Film.objects.all()
    films = all_films[::-1]
    context = {
        'caption': 'Лучшие фильмы',
        'page': 'Главная страница',
        'layout_data': {
            'home': 'Главная страница',
            'add': 'Добавить фильм'
        },
        'films': films
    }
    return render(request, 'films/index.html', context)


def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    context = {
        'caption': 'Лучшие фильмы',
        'page': 'Подробнее',
        'layout_data': {
            'home': 'Главная страница',
            'add': 'Добавить фильм'
        },
        'film': film
    }
    return render(request, 'films/details.html', context)

def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные были заполненны некорректно'
    form = FilmForm()
    context = {
        'caption': 'Лучшие фильмы',
        'page': 'Добавить фильм',
        'layout_data': {
            'home': 'Главная страница',
            'add': 'Добавить фильм'
        },
        'form': form,
        'error': error
    }
    return render(request, 'films/add_film.html', context)

