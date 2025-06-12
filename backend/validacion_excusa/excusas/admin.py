from django.contrib import admin
from .models import ExcusaMedica, CursoAfectado

@admin.register(ExcusaMedica)
class ExcusaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id_excusa', 'id_estudiante', 'fecha_inicio_ausencia', 'fecha_fin_ausencia', 'estado')
    list_filter = ('estado',)
    search_fields = ('id_estudiante__nombre_completo', 'motivo')


@admin.register(CursoAfectado)
class CursoAfectadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_curso', 'codigo_curso', 'grupo', 'fecha_afectada', 'id_excusa')
    search_fields = ('nombre_curso', 'codigo_curso')
