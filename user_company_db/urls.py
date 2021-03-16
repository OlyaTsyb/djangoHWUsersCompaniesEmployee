from django.urls import path

from user_company_db.views import CompanyListCreateView, CompanyEmployeeCreate, UserUpdateDeleteCompany, \
    CompanyGetByNameView

urlpatterns = [
    path('', CompanyListCreateView.as_view()),
    path('/<str:name>', CompanyGetByNameView.as_view()),
    path('/<int:pk>', UserUpdateDeleteCompany.as_view()),
    path('/<int:pk>/employee', CompanyEmployeeCreate.as_view()),

]
