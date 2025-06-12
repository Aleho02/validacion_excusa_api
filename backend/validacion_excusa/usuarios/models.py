from django.db import models
from django.contrib.auth.models import User
from facultades.models import ProgramaAcademico

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo_estudiante = models.CharField(max_length=20, blank=True, null=True)
    programa = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.codigo_estudiante}"

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.cargo}"

class FuncionarioValidador(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    facultad = models.CharField(max_length=100)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.funcionario.user.username} - Validador de {self.facultad}"
