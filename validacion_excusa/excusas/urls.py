from django.urls import path
from .views import (
    ExcusaMedicaListCreateAPIView,
    ExcusaMedicaRetrieveUpdateDestroyAPIView,
    CursoAfectadoListCreateAPIView,
    CursoAfectadoRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('excusas/', ExcusaMedicaListCreateAPIView.as_view(), name='excusa-list-create'),
    path('excusas/<int:pk>/', ExcusaMedicaRetrieveUpdateDestroyAPIView.as_view(), name='excusa-detail'),

    path('cursos-afectados/', CursoAfectadoListCreateAPIView.as_view(), name='cursoafectado-list-create'),
    path('cursos-afectados/<int:pk>/', CursoAfectadoRetrieveUpdateDestroyAPIView.as_view(), name='cursoafectado-detail'),
]
