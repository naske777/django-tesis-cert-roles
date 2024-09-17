from django.contrib import admin
from .models import RoleToCertify

class RoleToCertifyAdmin(admin.ModelAdmin):
    list_display = ('name')  # Reemplaza con los nombres de los campos de tu modelo

# Registra el modelo RoleToCertify en el sitio administrativo con la clase ModelAdmin
admin.site.register(RoleToCertify, RoleToCertifyAdmin)