from rest_framework import serializers
from rest_framework.validators import UniqueValidator



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=4, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        return user;

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
