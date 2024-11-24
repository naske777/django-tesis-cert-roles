from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        - POST (crear): Permitir a cualquiera
        - Otros métodos: Requerir autenticación
        """
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_profile = UserProfile.objects.get(user=user)

            return Response({
                'access': str(refresh.access_token),
                'userId': user.id,
                'role': user_profile.role,
                'studentId': user_profile.student.id if user_profile.student else None
            })

        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
