from rest_framework import serializers
from .models import CaseFile, Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'author', 'body', 'created_at']
        read_only_fields = ['id', 'created_at', 'author']

class CaseListSerializer(serializers.ModelSerializer):
    last_note = serializers.SerializerMethodField()
    next_hearing_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"], required=False, allow_null=True)

    class Meta:
        model = CaseFile
        fields = ['id', 'client_name', 'case_number', 'court', 'status', 'next_hearing_date', 'created_at', 'last_note']
        read_only_fields = ['created_at']

    def get_last_note(self, obj):
        note = obj.notes.order_by('-created_at').first()
        return {'id': note.id, 'body': note.body, 'created_at': note.created_at} if note else None

class CaseCreateSerializer(serializers.ModelSerializer):
    next_hearing_date = serializers.DateField(required=False, allow_null=True)
    class Meta:
        model = CaseFile
        fields = ['client_name', 'case_number', 'court', 'status', 'next_hearing_date']