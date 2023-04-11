from django.http import Http404, HttpResponse, HttpResponseRedirect
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


def add(request):
    title = request.POST.get("title")
    year = request.POST.get("year")
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect("/movies")

    return render(request, "movies/add.html")


def delete(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except movie.DoesNotExist:
        raise Http404("Movie does not exist")
    movie.delete()
    return HttpResponseRedirect("/movies")
