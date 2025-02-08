from django.urls import path
from .views import DashboardView, EntryDetalView, CreateEntryView, DeleteEntryView

urlpatterns = [
    # path('', WelcomeView.as_view(), name='welcome'),
    path('dashboard/', DashboardView.as_view(), name = 'blog-dashboard'),
    path('entry/<int:pk>', EntryDetalView.as_view(), name = 'entry-detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name = 'create_entry'),
    path('delete/<int:pk>/', DeleteEntryView.as_view(), name='delete-entry'),
]