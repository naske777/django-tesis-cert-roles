from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register(r'RoleToCertify', RoleToCertifyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]