from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from employee.permissions import ReadOnly, IsAdminUser


class BaseModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ReadOnly | IsAdminUser]
    ordering_fields = "__all__"
    ordering = ["-id"]
