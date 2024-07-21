from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated


class RoleToCertifyViewSet(viewsets.ModelViewSet):
    queryset = RoleToCertify.objects.all()
    serializer_class = RoleToCertifySerializer
    permission_classes = [IsAuthenticated]

