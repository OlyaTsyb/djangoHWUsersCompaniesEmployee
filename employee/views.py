from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Employee

from .serializers import EmployeeSerializer


class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeGetBySurname(ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        surname = self.kwargs.get('surname')
        queryset = Employee.objects.filter(surname__exact=surname)
        return queryset


class EmployeeUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
