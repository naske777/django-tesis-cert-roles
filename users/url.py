from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import UserViewSet, LoginView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
]
