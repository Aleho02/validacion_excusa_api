from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import ExcusaMedica, CursoAfectado
from usuarios.models import Estudiante
from facultades.models import Facultad, ProgramaAcademico
from datetime import date
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class ExcusasTests(APITestCase):
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
        
        # Crear datos de prueba para excusa médica
        self.excusa_data = {
            "fecha_inicio_ausencia": "2024-03-15",
            "fecha_fin_ausencia": "2024-03-16",
            "motivo": "Prueba de excusa médica",
            "estado": "pendiente",
            "id_estudiante": self.estudiante.id_estudiante
        }
        
        # Crear archivo de prueba
        self.archivo_prueba = SimpleUploadedFile(
            "test.pdf",
            b"contenido del archivo",
            content_type="application/pdf"
        )

    def test_crear_excusa(self):
        """Prueba la creación de una excusa médica"""
        url = reverse('excusa-list-create')
        data = self.excusa_data.copy()
        data['archivo_adjunto'] = self.archivo_prueba
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ExcusaMedica.objects.count(), 1)
        self.assertEqual(ExcusaMedica.objects.get().motivo, 'Prueba de excusa médica')

    def test_listar_excusas(self):
        """Prueba listar excusas médicas"""
        ExcusaMedica.objects.create(
            fecha_inicio_ausencia="2024-03-15",
            fecha_fin_ausencia="2024-03-16",
            motivo="Prueba de excusa médica",
            estado="pendiente",
            id_estudiante=self.estudiante
        )
        url = reverse('excusa-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalle_excusa(self):
        """Prueba obtener detalle de una excusa"""
        excusa = ExcusaMedica.objects.create(
            fecha_inicio_ausencia="2024-03-15",
            fecha_fin_ausencia="2024-03-16",
            motivo="Prueba de excusa médica",
            estado="pendiente",
            id_estudiante=self.estudiante
        )
        url = reverse('excusa-detail', args=[excusa.id_excusa])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['motivo'], 'Prueba de excusa médica')

    def test_actualizar_excusa(self):
        """Prueba actualizar una excusa"""
        excusa = ExcusaMedica.objects.create(
            fecha_inicio_ausencia="2024-03-15",
            fecha_fin_ausencia="2024-03-16",
            motivo="Prueba de excusa médica",
            estado="pendiente",
            id_estudiante=self.estudiante
        )
        url = reverse('excusa-detail', args=[excusa.id_excusa])
        data_actualizada = {
            "motivo": "Motivo actualizado"
        }
        response = self.client.patch(url, data_actualizada, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['motivo'], 'Motivo actualizado')

    def test_eliminar_excusa(self):
        """Prueba eliminar una excusa"""
        excusa = ExcusaMedica.objects.create(
            fecha_inicio_ausencia="2024-03-15",
            fecha_fin_ausencia="2024-03-16",
            motivo="Prueba de excusa médica",
            estado="pendiente",
            id_estudiante=self.estudiante
        )
        url = reverse('excusa-detail', args=[excusa.id_excusa])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ExcusaMedica.objects.count(), 0)

    def test_crear_curso_afectado(self):
        """Prueba la creación de un curso afectado"""
        excusa = ExcusaMedica.objects.create(
            fecha_inicio_ausencia="2024-03-15",
            fecha_fin_ausencia="2024-03-16",
            motivo="Prueba de excusa médica",
            estado="pendiente",
            id_estudiante=self.estudiante
        )
        url = reverse('cursoafectado-list-create')
        curso_data = {
            "nombre_curso": "Curso Test",
            "codigo_curso": "CT101",
            "grupo": "A",
            "fecha_afectada": "2024-03-15",
            "id_excusa": excusa.id_excusa
        }
        response = self.client.post(url, curso_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CursoAfectado.objects.count(), 1)
        self.assertEqual(CursoAfectado.objects.get().nombre_curso, 'Curso Test') 