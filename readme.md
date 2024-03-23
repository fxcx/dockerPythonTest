
# actualizar

# Doker - PYthon-Django

## este contenedor

- Atravez de las imagenes de docker, python. Va hacer un equipo ajeno al nuestro

- Modelo de stack MTV

## ENTORNO DE DESARROLLO

### runserver

- python manage.py runserver --settings=config.settings.develop

## BASE DE DATOS DEFAULT

### makemigrations

- python manage.py makemigrations tasks --settings=config.settings.develop

### creamos los modelos con la config para develop

python manage.py migrations tasks --settings=config.settings.develop

## instalacion de tealwind

-pip install django-tailwind

-pip install 'django-tailwind[reload]'

-pip freeze > requirements.txt

- INSTALLED_APPS = [
   Django apps
  'tailwind',
]
-python manage.py tailwind init --settings=config.settings.base o dvelop no me acuerdo tengo que cheakearlo

-INTERNAL_IPS = [
    "127.0.0.1",
]

-python manage.py tailwind install --settings=theme.static_src.package.json

```html
-{% load static tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>
```

-INSTALLED_APPS = [
   Django apps
  'tailwind',
  'theme',
  'django_browser_reload'
]

- Esto es un [mas sobre la configuracion de django con tealwind paso a paso, bien redactado](https://django-tailwind.readthedocs.io/en/latest/installation.html)

- en nuestra config/urls.py agregamos la ruta para el modo watch y ver nuestros cambios reflejados para mejor productividad..
path("__reload__/", include("django_browser_reload.urls")),

## ENTORNO DE PRODUCTIONS

## BASE DE DATOS POSTGRESQL
