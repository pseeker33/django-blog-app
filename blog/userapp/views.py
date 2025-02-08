from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class WelcomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog-dashboard')  # If authenticaded, go Dashboard
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
            return redirect('blog-dashboard')
        return render(request, 'userapp/register.html', {'form': form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'userapp/profile.html', context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'userapp/profile.html', context)