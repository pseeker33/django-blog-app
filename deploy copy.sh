#!/bin/bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Establecer el PYTHONPATH
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src/blog

# 3. Aplicar migraciones
cd blog
python manage.py migrate

# 4. Crear superusuario (solo si no existe)
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

# 5. Recopilar archivos estáticos
python manage.py collectstatic --noinput

# 6. Iniciar Gunicorn
gunicorn blog.wsgi:application --bind 0.0.0.0:$PORT