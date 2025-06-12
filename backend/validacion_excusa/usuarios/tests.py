from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Estudiante, FuncionarioValidador
from facultades.models import Facultad, ProgramaAcademico
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class UsuariosTests(APITestCase):
    def setUp(self):
        # Crear usuario para autenticación
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Obtener token
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
        # Crear datos de prueba
        self.facultad = Facultad.objects.create(
            nombre_facultad="Facultad de Prueba"
        )
        self.programa = ProgramaAcademico.objects.create(
            nombre_programa="Programa de Prueba",
            nivel="pregrado",
            id_facultad=self.facultad
        )
        
        # Crear estudiante de prueba
        self.estudiante_data = {
            "nombre_completo": "Estudiante Test",
            "codigo_estudiante": "123456",
            "correo": "test@ucundinamarca.edu.co",
            "id_programa": self.programa.id_programa
        }
        
        # Crear funcionario de prueba
        self.funcionario_data = {
            "nombre_completo": "Funcionario Test",
            "correo_institucional": "funcionario@ucundinamarca.edu.co",
            "dependencia": "Dependencia Test"
        }

    def test_crear_estudiante(self):
        """Prueba la creación de un estudiante"""
        url = reverse('estudiante-list-create')
        response = self.client.post(url, self.estudiante_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estudiante.objects.count(), 1)
        self.assertEqual(Estudiante.objects.get().nombre_completo, 'Estudiante Test')

    def test_listar_estudiantes(self):
        """Prueba listar estudiantes"""
        estudiante = Estudiante.objects.create(
            nombre_completo=self.estudiante_data['nombre_completo'],
            codigo_estudiante=self.estudiante_data['codigo_estudiante'],
            correo=self.estudiante_data['correo'],
            id_programa=self.programa
        )
        url = reverse('estudiante-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalle_estudiante(self):
        """Prueba obtener detalle de un estudiante"""
        estudiante = Estudiante.objects.create(
            nombre_completo=self.estudiante_data['nombre_completo'],
            codigo_estudiante=self.estudiante_data['codigo_estudiante'],
            correo=self.estudiante_data['correo'],
            id_programa=self.programa
        )
        url = reverse('estudiante-detail', args=[estudiante.id_estudiante])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_completo'], self.estudiante_data['nombre_completo'])

    def test_actualizar_estudiante(self):
        """Prueba actualizar un estudiante"""
        estudiante = Estudiante.objects.create(
            nombre_completo=self.estudiante_data['nombre_completo'],
            codigo_estudiante=self.estudiante_data['codigo_estudiante'],
            correo=self.estudiante_data['correo'],
            id_programa=self.programa
        )
        url = reverse('estudiante-detail', args=[estudiante.id_estudiante])
        data_actualizada = self.estudiante_data.copy()
        data_actualizada['nombre_completo'] = 'Estudiante Actualizado'
        response = self.client.put(url, data_actualizada, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_completo'], 'Estudiante Actualizado')

    def test_eliminar_estudiante(self):
        """Prueba eliminar un estudiante"""
        estudiante = Estudiante.objects.create(
            nombre_completo=self.estudiante_data['nombre_completo'],
            codigo_estudiante=self.estudiante_data['codigo_estudiante'],
            correo=self.estudiante_data['correo'],
            id_programa=self.programa
        )
        url = reverse('estudiante-detail', args=[estudiante.id_estudiante])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Estudiante.objects.count(), 0)

    def test_crear_funcionario(self):
        """Prueba la creación de un funcionario validador"""
        url = reverse('funcionario-list-create')
        response = self.client.post(url, self.funcionario_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FuncionarioValidador.objects.count(), 1)
        self.assertEqual(FuncionarioValidador.objects.get().nombre_completo, 'Funcionario Test')

    def test_listar_funcionarios(self):
        """Prueba listar funcionarios"""
        FuncionarioValidador.objects.create(**self.funcionario_data)
        url = reverse('funcionario-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalle_funcionario(self):
        """Prueba obtener detalle de un funcionario"""
        funcionario = FuncionarioValidador.objects.create(**self.funcionario_data)
        url = reverse('funcionario-detail', args=[funcionario.id_funcionario])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_completo'], self.funcionario_data['nombre_completo'])

    def test_actualizar_funcionario(self):
        """Prueba actualizar un funcionario"""
        funcionario = FuncionarioValidador.objects.create(**self.funcionario_data)
        url = reverse('funcionario-detail', args=[funcionario.id_funcionario])
        data_actualizada = self.funcionario_data.copy()
        data_actualizada['nombre_completo'] = 'Funcionario Actualizado'
        response = self.client.put(url, data_actualizada, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_completo'], 'Funcionario Actualizado')

    def test_eliminar_funcionario(self):
        """Prueba eliminar un funcionario"""
        funcionario = FuncionarioValidador.objects.create(**self.funcionario_data)
        url = reverse('funcionario-detail', args=[funcionario.id_funcionario])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FuncionarioValidador.objects.count(), 0) 