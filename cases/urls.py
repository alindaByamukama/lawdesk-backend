from django.urls import path
from .views import CaseListCreateView, CaseNoteCreateView

urlpatterns = [
    path('cases/', CaseListCreateView.as_view(), name='case-list-create'),
    path('cases/<int:pk>/notes/', CaseNoteCreateView.as_view(), name='case-note-create'),
]