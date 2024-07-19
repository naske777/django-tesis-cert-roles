from rest_framework import serializers
from .models import RoleToCertify

class RoleToCertifySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleToCertify
        fields = '__all__'
