from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

