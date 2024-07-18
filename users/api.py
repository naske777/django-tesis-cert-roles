from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

