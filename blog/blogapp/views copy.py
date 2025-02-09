from django.shortcuts import redirect, render
from .models import Entry
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy # Para la redirección después de eliminar

class DashboardView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'blogapp/dashboard.html'
    context_object_name = 'dashboard'
    ordering = ['-entry_date']
    paginate_by = 6

class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'blogapp/entry_detail.html'
    context_object_name = 'entry-detail'

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'blogapp/create_entry.html'
    fields = ['entry_title', 'entry_text']
    def form_valid(self,form):
        form.instance.entry_autor = self.request.user
        return super().form_valid(form)

class DeleteEntryView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'blogapp/delete_entry.html'  # Template de confirmación
    success_url = reverse_lazy('blog-dashboard')  # Redirige a la página principal

    def get_queryset(self): # Solo permite eliminar sus propios posts
        queryset = super().get_queryset()
        return queryset.filter(entry_autor=self.request.user)