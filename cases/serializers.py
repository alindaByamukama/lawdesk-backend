from rest_framework import serializers
from .model import CaseFile, Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'case', 'author', 'body', 'created_at']

class CaseFileSerializer(serializers.ModelSerializer):
    last_note = serializers.SerializerMethodField()

    class Meta:
        model = CaseFile
        fields = ['id', 'owner', 'client_name', 'case_number', 'court', 'status', 'next_hearing_date', 'created_at', 'last_note']

    def get_last_note(self, obj):
        note = obj.notes.order_by('-created_at').first()
        return {'id': note.id, 'body': note.body, 'created_at': note.created_at} if note else None