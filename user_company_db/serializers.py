from rest_framework.serializers import ModelSerializer

from employee.serializers import EmployeeSerializer
from user_company_db.models import UserCompany


class UserCompanySerializer(ModelSerializer):
    employee = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = UserCompany
        fields = ['id', 'name', 'country', 'city', 'employee']
