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
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        UserProfile.objects.create(user=user, **profile_data)
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
