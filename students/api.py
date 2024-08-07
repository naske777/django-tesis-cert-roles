from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if order:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)

        return queryset