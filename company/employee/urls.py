from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from employee.views import EmployeeViewSet, UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = format_suffix_patterns(router.urls)
