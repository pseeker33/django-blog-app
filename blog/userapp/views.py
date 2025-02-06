from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import RegistrationForm

class WelcomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog-home')  # If authenticaded, go Home
        return render(request, 'blogapp/welcome.html')
    
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'userapp/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog-home')
        return render(request, 'userapp/register.html', {'form': form})
