from django.db import models

class FacultyTypes(models.TextChoices):
    FACULTY1 = 'faculty1', 'Facultad 1'
    FACULTY2 = 'faculty2', 'Facultad 2'
    FACULTY3 = 'faculty3', 'Facultad 3'
    FACULTY4 = 'faculty4', 'Facultad 4'
    FTE = 'fte', 'FTE'

class SemesterTypes(models.TextChoices):
    UNO = '1', '1'
    DOS = '2', '2'

class Students(models.Model):
    name = models.TextField()
    solapin = models.TextField()
    faculty = models.CharField(max_length=10, choices=FacultyTypes.choices)
    center = models.TextField()
    year = models.IntegerField()
    group = models.IntegerField()
    semester = models.CharField(max_length=1, choices=SemesterTypes.choices)
    stage = models.TextField()
    roles = models.ManyToManyField('rolesToCertify.RoleToCertify', related_name='students', blank=True)    