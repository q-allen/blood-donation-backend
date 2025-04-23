from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)  # Made optional

    class Meta:
        model = CustomUser
        fields = [
            "first_name", "middle_name", "last_name", "username",
            "contact", "address", "gender", "email", "password", "confirm_password"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "middle_name": {"required": False, "allow_null": True},
        }

    def validate(self, data):
        # Only check confirm_password if provided
        if data.get("confirm_password") and data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)  # Safely remove confirm_password
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid credentials"})
        
        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Invalid credentials"})
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        return {
            "access": access_token,  # Match SigninPage
            "refresh": refresh_token
        }