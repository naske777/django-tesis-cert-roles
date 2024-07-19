from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Clases de Enumeración (TextChoices)
class BaseEvaluationsTypes(models.TextChoices):
    GOOD = 'good', 'Bien'
    REGULAR = 'regular', 'Regular'
    BAD = 'bad', 'Mal'

class CompleteEvaluationsTypes(BaseEvaluationsTypes):
    EXCELLENT = 'excellent', 'Excelente'

class GradingScaleTypes(models.TextChoices):
    HIGHT = 'hight', 'Alto'
    MEDIUM = 'medium', 'Medio'
    LOW = 'low', 'Bajo'

class SpecificCompetenciesTypes(models.TextChoices):
    NOT_DEVELOPED = 'not_developed', 'No desarrollada'
    LOW_DEVELOPMENT = 'low_development', 'Bajo desarrollo'
    MEDIUM_DEVELOPMENT = 'medium_development', 'Desarrollo medio'
    DEVELOPED = 'developed', 'Desarrollada'

# Modelo Principal
class Record(models.Model):
    proposedLvl = models.TextField()
    student = models.ForeignKey('Students', on_delete=models.CASCADE, related_name='records')

# Modelos Relacionados
class Task(models.Model):
    name = models.TextField()
    endingDate = models.DateField()
    complexity = models.CharField(max_length=5, choices=GradingScaleTypes.choices)
    criticality = models.CharField(max_length=5, choices=GradingScaleTypes.choices)
    evaluation = models.CharField(max_length=9, choices=CompleteEvaluationsTypes.choices)
    evidence = models.TextField()
    observations = models.TextField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='tasks')

class Evaluations(models.Model):
    performance = models.CharField(max_length=9, choices=CompleteEvaluationsTypes.choices)
    workday = models.CharField(max_length=9, choices=BaseEvaluationsTypes.choices)
    regulation = models.CharField(max_length=9, choices=BaseEvaluationsTypes.choices)
    otherActivities = models.CharField(max_length=9, choices=CompleteEvaluationsTypes.choices)
    evaluation = models.CharField(max_length=9, choices=CompleteEvaluationsTypes.choices)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='evaluations')

class GenericCompetencies(models.Model): 
    name = models.TextField()
    level = models.CharField(max_length=5, choices=GradingScaleTypes.choices)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='generic_competencies')

class SpecificCompetencies(models.Model): 
    name = models.TextField()
    description = models.TextField()
    evaluation = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)])
    argumentation = models.TextField()
    lvl = models.CharField(max_length=5, choices=SpecificCompetenciesTypes.choices)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='specific_competencies')

class Diagnosis(models.Model): 
    knowledge = models.TextField()
    isPreferRole = models.BooleanField()
    isPerformedRole = models.BooleanField()
    preferValue = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    performedTime = models.IntegerField()  # in months
    rolKnowledge = models.TextField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='diagnoses')