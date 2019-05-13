from django.urls import path, include
from .views import ListNotesView

urlpatterns = [
    path('', ListNotesView.as_view(), name='list-notes')
]