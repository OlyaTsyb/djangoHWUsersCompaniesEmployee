from rest_framework.serializers import ModelSerializer

from employee.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'age', 'company']
