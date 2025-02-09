from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import View

class WelcomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog-dashboard')  # If authenticaded, go Dashboard
        return render(request, 'blogapp/welcome.html')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_dashboard_link'] = False
        context['show_create_link'] = False
        context['show_profile_link'] = False
        return context

class RegisterView(TemplateView):
    template_name = 'userapp/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistrationForm()
        context['show_register_link'] = False
        context['show_login_link'] = True
        context['show_dashboard_link'] = False
        context['show_create_link'] = False
        context['show_profile_link'] = False
        return context

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog-dashboard')
        
        # Si el formulario no es válido, reutilizamos get_context_data
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
        
# class RegisterView(View):
#     def get(self, request):
#         form = RegistrationForm()
#         return render(request, 'userapp/register.html', {'form': form})

#     def post(self, request):
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = request.POST['username']
#             password = request.POST['password1']
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return redirect('blog-dashboard')
#         return render(request, 'userapp/register.html', {'form': form})
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['show_dashboard_link'] = False
#         context['show_create_link'] = False
#         context['show_profile_link'] = False
#         return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_dashboard_link'] = True
        context['show_create_link'] = True
        context['show_profile_link'] = False

        # Add forms to the context
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)
        context['u_form'] = u_form
        context['p_form'] = p_form
        return context
    
    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

        # Si el formulario no es válido, añadir al contexto
        context = self.get_context_data(**kwargs)
        context['u_form'] = u_form
        context['p_form'] = p_form
        return self.render_to_response(context)
    
    