from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import CaseFile, Note
from .serializers import CaseListSerializer, CaseCreateSerializer, NoteSerializer
