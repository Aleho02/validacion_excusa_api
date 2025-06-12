from rest_framework import generics
from .models import Estudiante, FuncionarioValidador
from .serializers import EstudianteSerializer, FuncionarioValidadorSerializer

# Estudiantes
class EstudianteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Funcionarios Validadores
class FuncionarioValidadorListCreateAPIView(generics.ListCreateAPIView):
    queryset = FuncionarioValidador.objects.all()
    serializer_class = FuncionarioValidadorSerializer

class FuncionarioValidadorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuncionarioValidador.objects.all()
    serializer_class = FuncionarioValidadorSerializer
