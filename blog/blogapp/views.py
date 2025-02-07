from django.shortcuts import redirect, render
from django.views.generic import View, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'blogapp/home.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 6

class EntryDetalView(LoginRequiredMixin, DetailView):
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