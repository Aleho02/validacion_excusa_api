from rest_framework import serializers
from .models import ExcusaMedica, CursoAfectado

class CursoAfectadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoAfectado
        fields = ['id_curso_afectado', 'nombre_curso', 'codigo_curso', 'grupo', 'fecha_afectada', 'id_excusa']

class ExcusaMedicaSerializer(serializers.ModelSerializer):
    cursos_afectados = CursoAfectadoSerializer(many=True, read_only=True)
    archivo_adjunto = serializers.FileField()

    class Meta:
        model = ExcusaMedica
        fields = [
            'id_excusa',
            'fecha_solicitud',
            'fecha_inicio_ausencia',
            'fecha_fin_ausencia',
            'motivo',
            'archivo_adjunto',
            'estado',
            'observaciones_validacion',
            'id_estudiante',
            'cursos_afectados',
        ]
