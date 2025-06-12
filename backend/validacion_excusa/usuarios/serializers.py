from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Estudiante, Funcionario, FuncionarioValidador

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class EstudianteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Estudiante
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Funcionario
        fields = '__all__'

class FuncionarioValidadorSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only=True)

    class Meta:
        model = FuncionarioValidador
        fields = '__all__'
