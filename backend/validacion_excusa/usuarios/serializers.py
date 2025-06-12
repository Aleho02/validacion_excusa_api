from rest_framework import serializers
from .models import Estudiante, FuncionarioValidador

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id_estudiante', 'nombre_completo', 'codigo_estudiante', 'correo', 'id_programa']

class FuncionarioValidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioValidador
        fields = ['id_funcionario', 'nombre_completo', 'correo_institucional', 'dependencia']
