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
