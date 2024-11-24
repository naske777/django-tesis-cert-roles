from django.test import TestCase
from .models import Students, FacultyTypes, SemesterTypes
from rolesToCertify.models import RoleToCertify

class StudentsTest(TestCase):
    def setUp(self):
        self.role = RoleToCertify.objects.create(name='Test Role')
        
    def test_student_creation(self):
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
        student.roles.add(self.role)
        
        self.assertEqual(student.name, 'Test Student')
        self.assertEqual(student.solapin, 'T123456')
        self.assertEqual(student.faculty, FacultyTypes.FACULTY1)
        self.assertTrue(self.role in student.roles.all())
        
    def test_unique_solapin(self):
        Students.objects.create(
            name='Student 1',
            solapin='T123456',
            faculty=FacultyTypes.FACULTY1,
            center='Test Center',
            year=2023,
            group=1,
            semester=SemesterTypes.UNO,
            stage='Test Stage'
        )
        
        with self.assertRaises(Exception):
            Students.objects.create(
                name='Student 2',
                solapin='T123456',  # Duplicate solapin
                faculty=FacultyTypes.FACULTY1,
                center='Test Center',
                year=2023,
                group=1,
                semester=SemesterTypes.UNO,
                stage='Test Stage'
            )
