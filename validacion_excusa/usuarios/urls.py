from django.urls import path
from .views import (
    EstudianteListCreateAPIView,
    EstudianteRetrieveUpdateDestroyAPIView,
    FuncionarioValidadorListCreateAPIView,
    FuncionarioValidadorRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Estudiantes
    path('estudiantes/', EstudianteListCreateAPIView.as_view(), name='estudiante-list-create'),
    path('estudiantes/<int:pk>/', EstudianteRetrieveUpdateDestroyAPIView.as_view(), name='estudiante-detail'),

    # Funcionarios Validadores
    path('funcionarios/', FuncionarioValidadorListCreateAPIView.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioValidadorRetrieveUpdateDestroyAPIView.as_view(), name='funcionario-detail'),
]
