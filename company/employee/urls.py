from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from employee.views import EmployeeViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"employees", EmployeeViewSet, basename="employees")

urlpatterns = format_suffix_patterns(router.urls)
