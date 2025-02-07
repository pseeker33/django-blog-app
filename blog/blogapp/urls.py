from django.urls import path
from .views import HomeView, EntryDetailView, CreateEntryView

urlpatterns = [
    # path('', WelcomeView.as_view(), name='welcome'),
    path('home/', HomeView.as_view(), name = 'blog-home'),
    path('entry/<int:pk>', EntryDetailView.as_view(), name = 'entry-detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name = 'create_entry'),
]