from django.contrib import admin
from .models import Facultad, ProgramaAcademico

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('id_facultad', 'nombre_facultad')
    search_fields = ('nombre_facultad',)


@admin.register(ProgramaAcademico)
class ProgramaAcademicoAdmin(admin.ModelAdmin):
    list_display = ('id_programa', 'nombre_programa', 'nivel', 'id_facultad')
    list_filter = ('nivel',)
    search_fields = ('nombre_programa',)
