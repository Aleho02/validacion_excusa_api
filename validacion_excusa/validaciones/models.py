from django.db import models
from usuarios.models import FuncionarioValidador
from excusas.models import ExcusaMedica

class Validacion(models.Model):
    RESULTADOS = [
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    id_validacion = models.AutoField(primary_key=True)
    fecha_validacion = models.DateField(auto_now_add=True)
    resultado = models.CharField(max_length=10, choices=RESULTADOS)
    comentarios = models.TextField(blank=True, null=True)
    id_funcionario = models.ForeignKey(FuncionarioValidador, on_delete=models.CASCADE, related_name='validaciones')
    id_excusa = models.OneToOneField(ExcusaMedica, on_delete=models.CASCADE, related_name='validacion')

    def __str__(self):
        return f"Validación de Excusa {self.id_excusa.id_excusa} - {self.resultado}"
