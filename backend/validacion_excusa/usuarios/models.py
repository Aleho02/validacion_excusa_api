from django.db import models
from facultades.models import ProgramaAcademico

class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=150)
    codigo_estudiante = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(unique=True)
    id_programa = models.ForeignKey(ProgramaAcademico, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre_completo} ({self.codigo_estudiante})"


class FuncionarioValidador(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=150)
    correo_institucional = models.EmailField(unique=True)
    dependencia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_completo} - {self.dependencia}"
