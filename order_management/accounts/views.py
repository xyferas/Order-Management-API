
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import User
from common.permission import IsAdmin
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Customer Registered Successfully"}, status=201
        )



from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomerViewSet(ModelViewSet):
    queryset = User.objects.filter(role='CUSTOMER')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
