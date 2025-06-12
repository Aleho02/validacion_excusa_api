from rest_framework import generics, permissions
from .models import ExcusaMedica, CursoAfectado
from .serializers import ExcusaMedicaSerializer, CursoAfectadoSerializer

class ExcusaMedicaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExcusaMedica.objects.all()
    serializer_class = ExcusaMedicaSerializer
    permission_classes = [permissions.IsAuthenticated]  # Cualquier usuario autenticado puede cargar/editar

class ExcusaMedicaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExcusaMedica.objects.all()
    serializer_class = ExcusaMedicaSerializer
    permission_classes = [permissions.IsAuthenticated]


class CursoAfectadoListCreateAPIView(generics.ListCreateAPIView):
    queryset = CursoAfectado.objects.all()
    serializer_class = CursoAfectadoSerializer
    permission_classes = [permissions.IsAuthenticated]

class CursoAfectadoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CursoAfectado.objects.all()
    serializer_class = CursoAfectadoSerializer
    permission_classes = [permissions.IsAuthenticated]
