from django.db import models
from usuarios.models import Estudiante

class ExcusaMedica(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    id_excusa = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_inicio_ausencia = models.DateField()
    fecha_fin_ausencia = models.DateField()
    motivo = models.TextField()
    archivo_adjunto = models.FileField(upload_to='excusa_pdfs/')  # Para almacenar PDFs
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    observaciones_validacion = models.TextField(blank=True, null=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='excusas')

    def __str__(self):
        return f"Excusa {self.id_excusa} - {self.id_estudiante.nombre_completo} ({self.estado})"


class CursoAfectado(models.Model):
    id_curso_afectado = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    codigo_curso = models.CharField(max_length=50)
    grupo = models.CharField(max_length=20)
    fecha_afectada = models.DateField()
    id_excusa = models.ForeignKey(ExcusaMedica, on_delete=models.CASCADE, related_name='cursos_afectados')

    def __str__(self):
        return f"{self.nombre_curso} ({self.codigo_curso}) - {self.fecha_afectada}"
