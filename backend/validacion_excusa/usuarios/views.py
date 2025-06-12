from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Estudiante, FuncionarioValidador, Funcionario
from .serializers import EstudianteSerializer, FuncionarioValidadorSerializer, FuncionarioSerializer
import re

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

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    email = request.data.get('email', '').lower()
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')

    # Validar que todos los campos requeridos estén presentes
    if not all([email, username, password, role]):
        return Response(
            {'error': 'Todos los campos son requeridos'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Validar el formato del correo institucional
    if not email.endswith('@ucundinamarca.edu.co'):
        return Response(
            {'error': 'Solo se permiten correos institucionales (@ucundinamarca.edu.co)'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Verificar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'El nombre de usuario ya está en uso'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {'error': 'El correo electrónico ya está registrado'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Crear el usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Crear el perfil según el rol
        if role == 'estudiante':
            Estudiante.objects.create(user=user)
        elif role == 'funcionario':
            Funcionario.objects.create(user=user)
        else:
            user.delete()
            return Response(
                {'error': 'Rol no válido'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'message': 'Usuario registrado exitosamente'},
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
        # Si algo sale mal, eliminar el usuario si fue creado
        if 'user' in locals():
            user.delete()
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
