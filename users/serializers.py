from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Students

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    student = serializers.PrimaryKeyRelatedField(
        queryset=Students.objects.all(),
        required=False,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'student']

def create(self, validated_data):
    from django.db import transaction
    
    student = validated_data.pop('student', None)
    
    with transaction.atomic():
        # Crear usuario
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        
        # Obtener o crear el perfil
        profile = UserProfile.objects.get_or_create(user=user)[0]
        
        # Si hay estudiante, actualizar el perfil
        if student:
            profile.student = student
            profile.role = 'student'  # Aseguramos que el rol sea estudiante
            profile.save()
        
        return user,profile
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('password', instance.password)
        instance.save()

        profile.role = profile_data.get('role', profile.role)
        profile.save()

        return instance
