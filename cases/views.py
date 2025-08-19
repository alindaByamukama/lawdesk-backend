from rest_framework import generics, permissions
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

    def get_queryset(self):
        return CaseFile.objects.filter(owner=self.request.user).order_by('id')
    
    def get_serializer_class(self):
        return CaseCreateSerializer if self.request.method == 'POST' else CaseListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
