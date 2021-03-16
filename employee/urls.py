from django.urls import path

from employee.views import EmployeeListCreateView, EmployeeUpdateDelete, EmployeeGetBySurname

urlpatterns = [
    path('', EmployeeListCreateView.as_view()),
    path('/<int:pk>', EmployeeUpdateDelete.as_view()),
    path('/<str:surname>', EmployeeGetBySurname.as_view())
]
