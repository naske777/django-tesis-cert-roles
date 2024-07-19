from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/login/', LoginView.as_view(), name='user_login'),

]