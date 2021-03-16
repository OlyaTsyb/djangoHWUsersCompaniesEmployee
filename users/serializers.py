from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from user_company_db.serializers import UserCompanySerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    user_company = UserCompanySerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'username', 'password', 'is_superuser', 'is_staff', 'is_active', 'user_company']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
