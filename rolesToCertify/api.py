from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *


class RolesToCertifyViewSet(viewsets.ModelViewSet):
    queryset = RolesToCertify.objects.all()
    serializer_class = RolesToCertifySerializer

