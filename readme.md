# Doker - PYthon -Djngo

## este contenedor

- es un equipo desde 0 , instalamos atravez de las imagenes de docker python. va hacer un equipo ajeno al nuestro

- Modelo de stack MTV

## ENTORNO DE DEV

### runserver

- python manage.py runserver --settings=config.settings.develop

## BASE DE DATOS DEFAULT

### a claramos makemigrations esta en la CPT Tasks en el entorno de desarrollo:develop en la ubicasion de las siguientes carpetas **config.settings.develop**

- python manage.py makemigrations tasks --settings=config.settings.develop

### creamos los modelos en el entorno de desarrollo

python manage.py migrations tasks --settings=config.settings.develop

## ENTORNO DE PRODUCTIONS

## BASE DE DATOS POSTGRESQL
