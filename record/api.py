from rest_framework import viewsets
from .models import (
    Record, Task, Evaluations, GenericCompetencies, SpecificCompetencies, Diagnosis
)
from .serializer import (
    RecordSerializer, TaskSerializer, EvaluationsSerializer,
    GenericCompetenciesSerializer, SpecificCompetenciesSerializer, DiagnosisSerializer
)

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer

class GenericCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = GenericCompetencies.objects.all()
    serializer_class = GenericCompetenciesSerializer

class SpecificCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = SpecificCompetencies.objects.all()
    serializer_class = SpecificCompetenciesSerializer

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer