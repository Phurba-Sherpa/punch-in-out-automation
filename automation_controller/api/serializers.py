from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=("email", "orange_hrm_username", "orange_hrm_password", "created_at")