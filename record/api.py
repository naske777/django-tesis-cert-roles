from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        return queryset

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        return queryset

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        return queryset

class GenericCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = GenericCompetencies.objects.all()
    serializer_class = GenericCompetenciesSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos
    
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        return queryset

class CompetencyViewSet(viewsets.ModelViewSet):
    queryset = Competency.objects.all()
    serializer_class = CompetencySerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        return queryset

class SpecificCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = SpecificCompetencies.objects.all()
    serializer_class = SpecificCompetenciesSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos

    def get_queryset(self):
        queryset = super().get_queryset()
        competency_id = self.request.query_params.get('competencyId', None)
        if competency_id:
            queryset = queryset.filter(competency_id=competency_id)
        return queryset

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'  # Permitir ordenación por todos los campos
    
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        return queryset