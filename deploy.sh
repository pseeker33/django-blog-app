#!/bin/bash

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta las migraciones
python manage.py migrate

# Recopila los archivos estáticos 
python manage.py collectstatic --noinput

# Inicia el servidor web (Gunicorn)
cd blog
gunicorn blog.wsgi:application