from rest_framework import serializers
from .models import Users


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Users
        fields = ['first_name','last_name','email','contact','password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.username = user.email
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()