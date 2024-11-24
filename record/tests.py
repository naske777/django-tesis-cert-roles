from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import (
    Record, Task, Evaluations, GenericCompetencies, 
    Competency, SpecificCompetencies, Diagnosis,
    BaseEvaluationsTypes, CompleteEvaluationsTypes, 
    GradingScaleTypes, SpecificCompetenciesTypes
)
from students.models import Students, FacultyTypes, SemesterTypes
from rolesToCertify.models import RoleToCertify
from datetime import date

class RecordModelsTest(TestCase):
    def setUp(self):
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
        self.role = RoleToCertify.objects.create(name='Test Role')

    def test_record_creation(self):
        record = Record.objects.create(
            proposedLvl='Test Level',
            students=self.student,
            role=self.role
        )
        self.assertEqual(record.proposedLvl, 'Test Level')
        self.assertEqual(record.students, self.student)

    def test_task_creation(self):
        task = Task.objects.create(
            name='Test Task',
            startDate=date.today(),
            endingDate=date.today(),
            complexity=GradingScaleTypes.MEDIUM,
            criticality=GradingScaleTypes.HIGHT,
            evaluation=CompleteEvaluationsTypes.GOOD,
            evidence='Test Evidence',
            observations='Test Observations',
            students=self.student,
            role=self.role
        )
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.complexity, GradingScaleTypes.MEDIUM)

    def test_specific_competencies_validation(self):
        competency = Competency.objects.create(
            name='Test Competency',
            level=SpecificCompetenciesTypes.DEVELOPED,
            students=self.student,
            role=self.role
        )
        
        specific_comp = SpecificCompetencies(
            competency=competency,
            description='Test Description',
            evaluation=6,  # Invalid value
            argumentation='Test Argumentation',
            lvl=SpecificCompetenciesTypes.DEVELOPED,
            role=self.role
        )
        
        with self.assertRaises(ValidationError):
            specific_comp.full_clean()
