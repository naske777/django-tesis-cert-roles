from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register(r'', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]