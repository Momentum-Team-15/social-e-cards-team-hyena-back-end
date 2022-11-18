from rest_framework import serializers
from models import User


# class UserRegistrationSerializer(BaseUserRegistration):
#     class Meta(BaseUserRegistration.Meta):
#         fields = ('email', 'name', 'last_name',
#                   'account_address', 'password',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
