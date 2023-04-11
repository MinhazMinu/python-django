# python-django

Django crud

###### Create virtual environment

-   First create virtual environment

```sh
python3 -m venv .venv
or
python -m venv .venv
```

-   Then activate virtual environment

```sh
. .venv/bin/activate
or from powershell
.venv\bin\Activate.ps1
```

###### Instal packages with pip

```sh
pip install django
```

we can see which packages it install by running

```sh
pip freeze
# output : asgiref==3.6.0
#          Django==4.2
#          sqlparse==0.4.3
#          tzdata==2023.3
```

###### Create django project

```sh
django-admin startproject movies .
```

###### Hello world

-   in urls.py we need to define a route.

```py
from django.contrib import admin
from django.urls import path
# import views.py file
from movies import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # new movies route
    path('movies/', views.movies),
]
```

-   create view.py file inside movies folder and write

```py
from django.http import HttpResponse

def movies(request):
    return HttpResponse('Hello, World!')
```

-   run local server

```sh
python manage.py runserver
```

and visit this url on browser http://127.0.0.1:8000/movies/
we will see **Hello World!**

###### First Template

-   Create a folder templates\movies
-   create movies.html inside the folder
-   write {{ movies }} in movies.html

-   change code in movies() method inside views.py

```py
from django.http import HttpResponse
from django.shortcuts import render

data = {"movies": ["movie1", "movie2"]}


def movies(request):
    return render(request, "movies/movies.html", data)


def home(request):
    return HttpResponse("This is home")
```

and visit this url on browser http://127.0.0.1:8000/movies/
we will see ["movie1", "movie2"]

-   customized movies.html file

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>My Movies</title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <ul>
            {% for movie in movies %}
            <li>
                <div class="movie">
                    <h2>{{ movie.title }}</h2>
                    <p>{{ movie.year }}</p>
                </div>
            </li>
            {% endfor %}
        </ul>
    </body>
</html>
```

###### DB migration

```sh
python manage.py migrate
```

-   Now create super user for admin panel

```sh
python manage.py createsuperuser
```

###### Create movie model

-   Create models.py inside model folder
-   then create model

```py
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
```

-   create migration file

```sh
python manage.py makemigrations movies
```

-   It will create a migrations folder. Inside that, there will be a 0001_initial.py file

*   if you want to see what sql will it generate by migration file

```sh
python manage.py sqlmigrate movies 0001
# 0001 is the migration file prefix
# output :
# BEGIN;
# --
# -- Create model Movie
# --
# CREATE TABLE "movies_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "year" integer NOT NULL);
# COMMIT;
```

-   Apply migration

```sh
python manage.py migrate
```

###### Add Movies Db table to the admin panel

-   Create a admin.py file inside movie folder

-   in admin.py file

```py
from .models import Movie
from django.contrib import admin

admin.site.register(Movie)
```

-   restart the server and go to http://127.0.0.1:8000/admin/
-   we will see movie DB

*   add a movie
*   This will show as movie object. which is not user friendly. To change that we need to use **str** magic method on models.py

```py
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} from {self.year}"
```

###### Show real data from DB in view

-   change movie function in views.py file

```py
def movies(request):
    data = Movie.objects.all()
    return render(request, "movies/movies.html", {"movies": data})
```

###### Details of a movie

-   create a details function on views.py

```py
def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
```

-   add the url in urls.py

```py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("movies/", views.movies),
    path("movies/<int:movie_id>", views.detail),
]
```

We can now add links to movies.html file

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>My Movies</title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <ul>
            {% for movie in movies %}
            <li>
                <div class="movie">
                    <h2><a href="{{movie.id}}">{{ movie.title }} </a></h2>
                    <p>{{ movie.year }}</p>
                </div>
            </li>
            {% endfor %}
        </ul>
    </body>
</html>
```
