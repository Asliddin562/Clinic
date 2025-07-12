from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    # is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'password2',
            'role', 'email', 'first_name', 'last_name',
        )
        extra_kwargs = {
            'email': {'required': True},
            'role': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name',]


class UserRoleUpdateSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['username', 'role']


class AccessTokenSerializer(serializers.Serializer):
    access = serializers.CharField()