from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models.fields import Field

def get_valid_order_fields(model):
    return [field.name for field in model._meta.get_fields() if isinstance(field, Field)]

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(Record)

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(Task)

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(Evaluations)

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset

class GenericCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = GenericCompetencies.objects.all()
    serializer_class = GenericCompetenciesSerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(GenericCompetencies)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset

class CompetencyViewSet(viewsets.ModelViewSet):
    queryset = Competency.objects.all()
    serializer_class = CompetencySerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(Competency)

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset

class SpecificCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = SpecificCompetencies.objects.all()
    serializer_class = SpecificCompetenciesSerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(SpecificCompetencies)

    def get_queryset(self):
        queryset = super().get_queryset()
        competency_id = self.request.query_params.get('competencyId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if competency_id:
            queryset = queryset.filter(competency_id=competency_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]
    valid_order_fields = get_valid_order_fields(Diagnosis)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('studentId', None)
        role_id = self.request.query_params.get('roleId', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if student_id and role_id:
            queryset = queryset.filter(students_id=student_id, role_id=role_id)
        
        if order and order in self.valid_order_fields:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        return queryset