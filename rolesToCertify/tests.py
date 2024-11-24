from django.test import TestCase
from .models import RoleToCertify
from students.models import Students, FacultyTypes, SemesterTypes

class RoleToCertifyTest(TestCase):
    def test_role_creation(self):
        role = RoleToCertify.objects.create(name='Test Role')
        self.assertEqual(role.name, 'Test Role')

    def test_role_student_relationship(self):
        role = RoleToCertify.objects.create(name='Test Role')
        student = Students.objects.create(
            name='Test Student',
            solapin='T123456',
            faculty=FacultyTypes.FACULTY1,
            center='Test Center',
            year=2023,
            group=1,
            semester=SemesterTypes.UNO,
            stage='Test Stage'
        )
        
        student.roles.add(role)
        self.assertTrue(role in student.roles.all())
        self.assertTrue(student in role.students.all())
