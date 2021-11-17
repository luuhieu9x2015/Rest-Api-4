# from rest_framework import serializers

# from apps.users.models import ClientModel
# from apps.users.serializers.user_serializers import UserListSerializer

# class ClientSerializer(serializers.ModelSerializer):

#     users = UserListSerializer(many=True, read_only=True)
#     class Meta:
#         model = ClientModel
#         fields = ['client_id','email', 'last_name_kanji', 'seconds_delivered_per_month', 'is_archived']

#         extra_kwargs = {
#             'client_id': {'required': False}
#         }

#     # class Meta:
#     #     model = ClientModel
#     #     fields = ['client_id', 'name', 'users', 'seconds_delivered_per_month', 'is_archived']

#     #     extra_kwargs = {
#     #         'client_id': {'required': False}
#     #     }

#     # def save(self, **kwargs):
#     #     client = ClientModel()
#     #     client.client_id = self.initial_data['client_id']
#     #     client.name = self.initial_data['name']
#     #     client.seconds_delivered_per_month = 0
#     #     client.is_archived = self.initial_data['is_archived']
#     #     client.save()
#     #     return client
