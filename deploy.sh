#!/bin/bash

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Aplicar migraciones
python blog/manage.py migrate

# 3. Crear superusuario (solo si no existe)
python -c "
import os
from django.contrib.auth.models import User

if not User.objects.filter(is_superuser=True).exists():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'password')
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuario creado: {username}')
else:
    print('Superusuario ya existe.')
"

# 4. Recopilar archivos estáticos
python blog/manage.py collectstatic --noinput

# 5. Iniciar el servidor web (Gunicorn)
cd blog
gunicorn blog.wsgi:application