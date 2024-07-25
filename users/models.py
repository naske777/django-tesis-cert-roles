from django.contrib.auth.models import User
from django.db import models
from students.models import Students
class RoleType(models.TextChoices):
    ADMIN = 'adm', 'Administrador'
    TUTOR = 'tutor', 'Tutor'
    STUDENT = 'student', 'Estudiante'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=RoleType.choices,
        default=RoleType.STUDENT
    )
    student = models.OneToOneField(Students, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

# Añade la propiedad al modelo User para acceder al perfil fácilmente
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
