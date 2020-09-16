from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = "__all__"

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs
