from django.urls import path

from .views import UserListCreateView, UserCompanyCreate, UserUpdateDeleteCompany, UserGetByName

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>', UserUpdateDeleteCompany.as_view()),
    path('/<str:email>', UserGetByName.as_view()),
    path('/<int:pk>/companies', UserCompanyCreate.as_view()),

]
