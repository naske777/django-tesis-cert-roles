from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializer import *
from users.models import UserProfile

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        """
        - POST (create): Allow anyone
        - Other methods: Require JWT authentication
        """
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id', None)
        order = self.request.query_params.get('order', None)
        order_by = self.request.query_params.get('order_by', 'asc')

        if user_id:
            try:
                user_profile = UserProfile.objects.get(user__id=user_id)
                if user_profile.role == 'tutor':
                    queryset = user_profile.tutor_students.all()
                else:
                    queryset = Students.objects.none()
            except UserProfile.DoesNotExist:
                queryset = Students.objects.none()

        if order:
            if order_by == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)

        return queryset