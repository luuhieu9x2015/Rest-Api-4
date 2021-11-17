from rest_framework import serializers

from apps.users.models import ClientModel, UsersModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['email', 'username', 'password']

class ClientSerialize(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ['client_id', 'seconds_delivered_per_month', 'is_archived']
        extra_kwargs = {
            'client_id': {'required': False}
        }



class ClientListSerialize(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = ClientModel
        fields = ['client_id', 'seconds_delivered_per_month', 'is_archived', 'users']

        extra_kwargs = {
            'client_id': {'required': False}
        }



class UserListSerializer(serializers.ModelSerializer):
    client = ClientSerialize(many=False)
    class Meta:
        model = UsersModel
        fields = ['user_id', 'email', 'last_name_kanji', 'first_name_kanji', 'client']
