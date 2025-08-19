from rest_framework import serializers
from .model import CaseFile, Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'case', 'author', 'body', 'created_at']
