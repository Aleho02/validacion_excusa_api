from rest_framework import serializers
from .models import Facultad, ProgramaAcademico

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ['id_facultad', 'nombre_facultad']


class ProgramaAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaAcademico
        fields = ['id_programa', 'nombre_programa', 'nivel', 'id_facultad']
