from django.contrib import admin
from .models import RoleToCertify

@admin.register(RoleToCertify)
class RoleToCertifyAdmin(admin.ModelAdmin):
    pass

