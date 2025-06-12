from django.db import models

class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre_facultad = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_facultad


class ProgramaAcademico(models.Model):
    NIVEL_CHOICES = [
        ('pregrado', 'Pregrado'),
        ('posgrado', 'Posgrado'),
        ('especializacion', 'Especialización'),
        ('maestria', 'Maestría'),
        ('doctorado', 'Doctorado'),
    ]

    id_programa = models.AutoField(primary_key=True)
    nombre_programa = models.CharField(max_length=150)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    id_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='programas')

    def __str__(self):
        return f"{self.nombre_programa} ({self.get_nivel_display()})"
