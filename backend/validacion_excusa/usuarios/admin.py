from django.contrib import admin
from .models import Estudiante, Funcionario, FuncionarioValidador

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('user', 'codigo_estudiante', 'programa')
    search_fields = ('user__username', 'codigo_estudiante')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'departamento')
    search_fields = ('user__username', 'cargo')

@admin.register(FuncionarioValidador)
class FuncionarioValidadorAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'facultad', 'fecha_asignacion')
    search_fields = ('funcionario__user__username', 'facultad')
