from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class JWTUserSerializer(serializers.ModelSerializer):
    permissions = serializers.SlugRelatedField(source="user_permissions", slug_field="codename", many=True, read_only=True)
    groups = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'username',
                  'email',
                  'is_active',
                  'is_staff',
                  'is_superuser',
                  'groups',
                  'permissions']
