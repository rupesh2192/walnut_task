# Create your views here.

from employee.mixins import BaseModelViewSet
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(BaseModelViewSet):
    """
    API endpoint that allows to List, Create, Update and Delete Movie objects.
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_staff=False)
    filterset_fields = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]


class UserViewSet(EmployeeViewSet):
    """
    API endpoint that allows to List, Create, Update and Delete Movie objects.
    """
    queryset = Employee.objects.filter(is_staff=True)

