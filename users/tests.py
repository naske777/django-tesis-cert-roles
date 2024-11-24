from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, RoleType
from students.models import Students, FacultyTypes, SemesterTypes

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Eliminar el perfil creado automáticamente
        UserProfile.objects.filter(user=self.user).delete()
        
        self.student = Students.objects.create(
            name='Test Student',
            solapin='T123456',
            faculty=FacultyTypes.FACULTY1,
            center='Test Center',
            year=2023,
            group=1,
            semester=SemesterTypes.UNO,
            stage='Test Stage'
        )

    def test_user_profile_creation(self):
        profile = UserProfile.objects.create(
            user=self.user,
            role=RoleType.STUDENT,
            student=self.student
        )
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.get_role_display(), 'Estudiante')
        self.assertEqual(profile.student.solapin, 'T123456')

    def test_user_profile_property(self):
        profile = self.user.profile
        self.assertIsInstance(profile, UserProfile)
        self.assertEqual(profile.role, RoleType.STUDENT)
