from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer
from common.permission import IsAdmin, IsCustomer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN' or user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(customer=user)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsCustomer()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
