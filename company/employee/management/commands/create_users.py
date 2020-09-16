from django.core.management import BaseCommand

from employee.models import Employee
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    This command will remove existing users and create an Admin and a Non-Admin user in the database.
    """
    help = "Create one Admin and one Non-Admin User"

    def handle(self, *args, **options):
        Employee.objects.filter(is_staff=True).delete()
        admin_user, _ = Employee.objects.get_or_create(username="admin", is_active=True, is_admin=True, is_staff=True)
        admin_user.set_password("admin")
        admin_user.save()

        user, _ = Employee.objects.get_or_create(username="test", is_active=True, is_staff=True)
        user.set_password("test")
        user.save()
        print("Hello")
        logger.info("Users added successfully")
