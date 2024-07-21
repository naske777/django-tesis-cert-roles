from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer
    permission_classes = [IsAuthenticated]

class GenericCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = GenericCompetencies.objects.all()
    serializer_class = GenericCompetenciesSerializer
    permission_classes = [IsAuthenticated]

class SpecificCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = SpecificCompetencies.objects.all()
    serializer_class = SpecificCompetenciesSerializer
    permission_classes = [IsAuthenticated]

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]
