from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, WelcomeView, ProfileView  

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # LOGOUT_REDIRECT_URL en settings se aplicará aquí
    path('welcome/', WelcomeView.as_view(), name='welcome'),  # Página de bienvenida
    path('profile/', ProfileView.as_view(), name='profile'),
]
