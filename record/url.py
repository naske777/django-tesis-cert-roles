from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RecordViewSet, TaskViewSet, EvaluationsViewSet,
    GenericCompetenciesViewSet, SpecificCompetenciesViewSet, DiagnosisViewSet
)

router = DefaultRouter()
router.register(r'records', RecordViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'evaluations', EvaluationsViewSet)
router.register(r'generic_competencies', GenericCompetenciesViewSet)
router.register(r'specific_competencies', SpecificCompetenciesViewSet)
router.register(r'diagnoses', DiagnosisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]