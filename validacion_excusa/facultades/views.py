from rest_framework import generics
from .models import Facultad, ProgramaAcademico
from .serializers import FacultadSerializer, ProgramaAcademicoSerializer

# Facultades
class FacultadListCreateAPIView(generics.ListCreateAPIView):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer


class FacultadRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer


# Programas Académicos
class ProgramaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProgramaAcademico.objects.all()
    serializer_class = ProgramaAcademicoSerializer


class ProgramaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgramaAcademico.objects.all()
    serializer_class = ProgramaAcademicoSerializer
