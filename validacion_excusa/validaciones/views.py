from rest_framework import generics, permissions
from .models import Validacion
from .serializers import ValidacionSerializer

class ValidacionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Validacion.objects.all()
    serializer_class = ValidacionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo autenticados pueden ver o validar

class ValidacionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Validacion.objects.all()
    serializer_class = ValidacionSerializer
    permission_classes = [permissions.IsAuthenticated]
