from django.urls import path
from .views import HomeView, EntryDetalView, CreateEntryView

urlpatterns = [
    # path('', WelcomeView.as_view(), name='welcome'),
    path('home/', HomeView.as_view(), name = 'blog-home'),
    path('entry/<int:pk>', EntryDetalView.as_view(), name = 'entry-detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name = 'create_entry'),
]