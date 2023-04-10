from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from accounts.models import Admin


class AddAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Admin
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def validate(self, attrs):
        validate_password(attrs.get('password'))
        return attrs

    def create(self, validated_data):
        admin = self.Meta.model.objects.create_admin(**self.validated_data)
        return admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'is_active', 'modified_at')
        read_only_fields = ('id', 'date_joined', 'modified_at')


class AdminMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'username', 'is_active')
        read_only_fields = ('id', 'username', 'is_active')
