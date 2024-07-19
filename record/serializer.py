from rest_framework import serializers
from .models import *

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluations
        fields = '__all__'

class GenericCompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericCompetencies
        fields = '__all__'

class SpecificCompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificCompetencies
        fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'