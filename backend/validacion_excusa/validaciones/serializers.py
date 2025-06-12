from rest_framework import serializers
from .models import Validacion

class ValidacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validacion
        fields = ['id_validacion', 'fecha_validacion', 'resultado', 'comentarios', 'id_funcionario', 'id_excusa']
