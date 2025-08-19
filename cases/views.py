from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import CaseFile, Note
from .serializers import CaseListSerializer, CaseCreateSerializer, NoteSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, 'owner_id', None) == request.user.id

class CaseListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CaseListSerializer
    filterset_fields = {'status': ['exact'], 'next_hearing_date': ['gte', 'lte']}
    search_fields = ['client_name', 'case_number']
    ordering_fields = ['next_hearing_date', 'created_at']

    def get_queryset(self):
        return CaseFile.objects.filter(owner=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        return CaseCreateSerializer if self.request.method == 'POST' else CaseListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CaseNoteCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        case_id = self.kwargs.get('pk')
        case = get_object_or_404(CaseFile, pk=case_id, owner=self.request.user)
        serializer.save(case=case, author=self.request.user)

class CaseDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = CaseFile.objects.all()
    serializer_class = CaseListSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.owner_id != self.request.user.id:
            raise NotFound("Case not found.")
        return obj
    
class CaseNoteListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(
            case_id=self.kwargs['pk'], case__owner=self.request.user).order_by('-created_at')