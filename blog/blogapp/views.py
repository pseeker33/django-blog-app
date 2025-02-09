from django.shortcuts import redirect, render
from .models import Entry
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class DashboardView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'blogapp/dashboard.html'
    context_object_name = 'dashboard'
    ordering = ['-entry_date']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_dashboard_link'] = False
        context['show_create_link'] = True
        context['show_profile_link'] = True
        return context

class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'blogapp/entry_detail.html'
    context_object_name = 'entry-detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_dashboard_link'] = True
        context['show_create_link'] = True
        context['show_profile_link'] = True
        return context

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'blogapp/create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self,form):
        form.instance.entry_autor = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_dashboard_link'] = True
        context['show_create_link'] = False
        context['show_profile_link'] = True
        return context

class DeleteEntryView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'blogapp/delete_entry.html'
    success_url = reverse_lazy('blog-dashboard')

    def get_queryset(self): # Solo permite eliminar sus propios posts
        queryset = super().get_queryset()
        return queryset.filter(entry_autor=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_dashboard_link'] = True
        context['show_create_link'] = True
        context['show_profile_link'] = True
        return context