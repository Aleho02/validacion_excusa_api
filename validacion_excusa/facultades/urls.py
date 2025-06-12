from django.urls import path
from .views import (
    FacultadListCreateAPIView,
    FacultadRetrieveUpdateDestroyAPIView,
    ProgramaListCreateAPIView,
    ProgramaRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Facultades
    path('facultades/', FacultadListCreateAPIView.as_view(), name='facultad-list-create'),
    path('facultades/<int:pk>/', FacultadRetrieveUpdateDestroyAPIView.as_view(), name='facultad-detail'),

    # Programas Académicos
    path('programas/', ProgramaListCreateAPIView.as_view(), name='programa-list-create'),
    path('programas/<int:pk>/', ProgramaRetrieveUpdateDestroyAPIView.as_view(), name='programa-detail'),
]
