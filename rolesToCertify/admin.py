from django.contrib import admin
from .models import RoleToCertify

class RoleToCertifyAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Corrected to be a tuple

# Register the model RoleToCertify with the admin site using the ModelAdmin class
admin.site.register(RoleToCertify, RoleToCertifyAdmin)