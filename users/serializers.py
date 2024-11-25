from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer(required=False)  # Hacer opcional

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {'role': 'student'})  # Valor por defecto
        # Crear usuario
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        # El perfil se crea automáticamente por la señal en signals.py
        # Solo actualizamos los datos del perfil
        if profile_data:
            for key, value in profile_data.items():
                setattr(user.profile, key, value)
            user.profile.save()
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('password', instance.password)
        instance.save()

        profile.role = profile_data.get('role', profile.role)
        profile.save()

        return instance
