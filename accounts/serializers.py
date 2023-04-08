from rest_framework import serializers

from accounts.models import Admin


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
