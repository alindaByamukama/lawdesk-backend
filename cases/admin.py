from django.contrib import admin
from .models import CaseFile, Note

# Register your models here.
@admin.register(CaseFile)
class CaseFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'case_number', 'court', 'status', 'next_hearing_date', 'created_at')
    search_fields = ('client_name', 'case_number', 'court', 'status')
    list_filter = ('status', 'next_hearing_date')
    ordering = ('-created_at',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'case', 'author', 'created_at')
    search_fields = ('case__client_name', 'author__username', 'body')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
