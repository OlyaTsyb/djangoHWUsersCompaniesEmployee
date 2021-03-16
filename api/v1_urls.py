from django.urls import path, include

urlpatterns = [
    path('/users', include('users.urls')),
    path('/company', include('user_company_db.urls')),
    path('/employee', include('employee.urls'))
]
