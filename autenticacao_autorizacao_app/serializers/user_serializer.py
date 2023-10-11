from django.contrib.auth.models import User
from rest_framework import serializers
import re


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, password):
        #pelo menos uma letra maiuscula
        if not re.match(r"^\d{6}$", password):
            raise serializers.ValidationError("A senha deve ser composta por apenas digitos e tenha exatamente 6 deles")
        return password
    
    def validate_email(self, email):
        #pelo menos uma letra maiuscula
        if not re.search('@gmail.com', email):
            raise serializers.ValidationError("O email deve ser @gmail")
        return email

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')