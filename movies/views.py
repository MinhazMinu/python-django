from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def movies(request):
    data = Movie.objects.all()
    return render(request, "movies/movies.html", {"movies": data})


def home(request):
    return HttpResponse("This is home")


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
