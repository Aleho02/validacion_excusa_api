from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Validacion
from usuarios.models import Estudiante, FuncionarioValidador
from excusas.models import ExcusaMedica
from facultades.models import Facultad, ProgramaAcademico
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class ValidacionesTests(APITestCase):
    def setUp(self):
        # Crear usuario para autenticación
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Obtener token
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
        # Crear datos necesarios para las pruebas
        self.facultad = Facultad.objects.create(
            nombre_facultad="Facultad de Prueba"
        )
        self.programa = ProgramaAcademico.objects.create(
            nombre_programa="Programa de Prueba",
            nivel="pregrado",
            id_facultad=self.facultad
        )
        self.estudiante = Estudiante.objects.create(
            nombre_completo="Estudiante Test",
            codigo_estudiante="123456",
            correo="test@ucundinamarca.edu.co",
            id_programa=self.programa
        )
        self.funcionario = FuncionarioValidador.objects.create(
            nombre_completo="Funcionario Test",
            correo_institucional="funcionario@ucundinamarca.edu.co",
            dependencia="Dependencia Test"
        )
        self.excusa = ExcusaMedica.objects.create(
            fecha_inicio_ausencia="2024-03-15",
            fecha_fin_ausencia="2024-03-16",
            motivo="Prueba de excusa médica",
            estado="pendiente",
            id_estudiante=self.estudiante
        )
        
        # Crear datos de prueba para validación
        self.validacion_data = {
            "resultado": "aprobada",
            "comentarios": "Prueba de validación",
            "id_funcionario": self.funcionario.id_funcionario,
            "id_excusa": self.excusa.id_excusa
        }

    def test_crear_validacion(self):
        """Prueba la creación de una validación"""
        url = reverse('validacion-list-create')
        response = self.client.post(url, self.validacion_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Validacion.objects.count(), 1)
        self.assertEqual(Validacion.objects.get().resultado, 'aprobada')

    def test_listar_validaciones(self):
        """Prueba listar validaciones"""
        Validacion.objects.create(
            resultado=self.validacion_data['resultado'],
            comentarios=self.validacion_data['comentarios'],
            id_funcionario=self.funcionario,
            id_excusa=self.excusa
        )
        url = reverse('validacion-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalle_validacion(self):
        """Prueba obtener detalle de una validación"""
        validacion = Validacion.objects.create(
            resultado=self.validacion_data['resultado'],
            comentarios=self.validacion_data['comentarios'],
            id_funcionario=self.funcionario,
            id_excusa=self.excusa
        )
        url = reverse('validacion-detail', args=[validacion.id_validacion])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['resultado'], self.validacion_data['resultado'])

    def test_actualizar_validacion(self):
        """Prueba actualizar una validación"""
        validacion = Validacion.objects.create(
            resultado=self.validacion_data['resultado'],
            comentarios=self.validacion_data['comentarios'],
            id_funcionario=self.funcionario,
            id_excusa=self.excusa
        )
        url = reverse('validacion-detail', args=[validacion.id_validacion])
        data_actualizada = self.validacion_data.copy()
        data_actualizada['resultado'] = 'rechazada'
        data_actualizada['comentarios'] = 'Validación actualizada'
        response = self.client.put(url, data_actualizada, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['resultado'], 'rechazada')

    def test_eliminar_validacion(self):
        """Prueba eliminar una validación"""
        validacion = Validacion.objects.create(
            resultado=self.validacion_data['resultado'],
            comentarios=self.validacion_data['comentarios'],
            id_funcionario=self.funcionario,
            id_excusa=self.excusa
        )
        url = reverse('validacion-detail', args=[validacion.id_validacion])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Validacion.objects.count(), 0)

    def test_validacion_excusa_unica(self):
        """Prueba que una excusa solo puede tener una validación"""
        Validacion.objects.create(
            resultado=self.validacion_data['resultado'],
            comentarios=self.validacion_data['comentarios'],
            id_funcionario=self.funcionario,
            id_excusa=self.excusa
        )
        url = reverse('validacion-list-create')
        response = self.client.post(url, self.validacion_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 