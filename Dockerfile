## imagen base
FROM python:3.12.2-alpine3.19

## resuelve el buffer para correr la app
ENV PYTHONUNBUFFERED=1

## donde va a estar nuestra app
WORKDIR /app

## actualizar lo que es los paquetes de la distribucion y actualizar paquetes de pip que hallamos instalodo nuevo
RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

## quiero que copies && pegues en el directorio actual
COPY ./requirements.txt ./

## instalar && actualizar  pip que esta en requirements.txt / aprovechemos el cache de docker
RUN pip install -r requirements.txt

## de este directorio copies todo y pegues en /app
COPY ./ ./

## ejecutar el proyecto / fuera del equipo / 
CMD ["python","manage.py","runserver","0.0.0.0:8000"]