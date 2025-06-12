from django.contrib import admin
from .models import Estudiante, FuncionarioValidador

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_estudiante', 'nombre_completo', 'codigo_estudiante', 'correo', 'id_programa')
    search_fields = ('nombre_completo', 'codigo_estudiante', 'correo')


@admin.register(FuncionarioValidador)
class FuncionarioValidadorAdmin(admin.ModelAdmin):
    list_display = ('id_funcionario', 'nombre_completo', 'correo_institucional', 'dependencia')
    search_fields = ('nombre_completo', 'correo_institucional', 'dependencia')
