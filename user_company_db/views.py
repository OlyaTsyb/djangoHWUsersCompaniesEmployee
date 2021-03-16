from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from .models import UserCompany

from user_company_db.serializers import UserCompanySerializer
from employee.serializers import EmployeeSerializer


class CompanyListCreateView(ListCreateAPIView):
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer


class CompanyGetByNameView(ListCreateAPIView):
    serializer_class = UserCompanySerializer

    def get_queryset(self):
        name = self.kwargs.get('name')
        queryset = UserCompany.objects.filter(name__exact=name)
        return queryset


class CompanyEmployeeCreate(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        id = self.kwargs.get('pk')
        company = get_object_or_404(UserCompany, pk=id)
        print(company)
        serializer.save(company=company)


class UserUpdateDeleteCompany(RetrieveUpdateDestroyAPIView):
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer
