from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

class ListNotesView(generics.ListCreateAPIView):
    
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)