from django.urls import path
from .views import CaseListCreateView, CaseNoteCreateView, CaseDetailView, CaseNoteListView

urlpatterns = [
    path('cases/', CaseListCreateView.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', CaseDetailView.as_view(), name='case-detail'),
    path('cases/<int:pk>/notes/', CaseNoteCreateView.as_view(), name='case-note-create'),
    path('cases/<int:pk>/notes/list/', CaseNoteListView.as_view(), name='case-note-list'),
]