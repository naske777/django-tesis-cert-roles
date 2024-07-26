from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'evaluations', EvaluationsViewSet)
router.register(r'generic_competencies', GenericCompetenciesViewSet)
router.register(r'specific_competencies', SpecificCompetenciesViewSet)
router.register(r'diagnoses', DiagnosisViewSet)
router.register(r'competency', CompetencyViewSet)
router.register(r'', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]