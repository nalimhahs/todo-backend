from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Note
        fields = ("title", "content", "isRemainder", "user")
    
    
class UserSerializer(serializers.ModelSerializer):

    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "notes")
