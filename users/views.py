from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView

from user_company_db.serializers import UserCompanySerializer
from users.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserGetByName(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        email = self.kwargs.get('email')
        queryset = UserModel.objects.filter(email__exact=email)
        return queryset


class UserCompanyCreate(CreateAPIView):
    serializer_class = UserCompanySerializer

    def perform_create(self, serializer):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=user_id)
        serializer.save(user=user)


class UserUpdateDeleteCompany(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCompanySerializer
