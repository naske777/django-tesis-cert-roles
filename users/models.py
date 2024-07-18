from django.db import models


class RoleType(models.TextChoices):
    ADMIN = 'adm', 'Administrador'
    TUTOR = 'tutor', 'Tutor'
    STUDENT = 'student', 'Estudiante'


class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    role = models.CharField(max_length=10, choices=RoleType.choices)
