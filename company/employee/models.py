from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UsersManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)


class EmployeeManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False)


class Employee(AbstractUser, BaseModel):
    is_admin = models.BooleanField(default=False)
    employees = EmployeeManager()
    users = UsersManager()

    class Meta:
        db_table = "employee"
