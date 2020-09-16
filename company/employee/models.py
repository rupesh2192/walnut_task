from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(AbstractUser, BaseModel):
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "employee"
