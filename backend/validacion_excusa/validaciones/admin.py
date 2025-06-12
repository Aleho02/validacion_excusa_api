from django.contrib import admin
from .models import Validacion

@admin.register(Validacion)
class ValidacionAdmin(admin.ModelAdmin):
    list_display = ('id_validacion', 'id_funcionario', 'id_excusa', 'resultado', 'fecha_validacion')
    list_filter = ('resultado',)
