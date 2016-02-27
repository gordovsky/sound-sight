from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'email', 'password', 'confirm_password',
                  'date_joined')
        read_only_fields = ('last_login', 'date_joined')

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instanse, validated_data):
            instanse.username = validated_data.get('username', instanse.username)
            instanse.email = validated_data.get('email', instanse.email)

            instanse.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instanse.set_password(password)
                instanse.save()

            # update_session_auth_hash(self.context.get('request'), instanse)

            return instanse
