from django.db.models import fields
from rest_framework import serializers

from apps.events.models import EventModel
from apps.users import models


# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventModel
#         fields = ['event_id', 'type', 'title', 'type']
#         extra_kwargs = {
#             'event_id': {'required': False}
#         }

# class ImgUrlSerializer(serializers.ModelSerializer):
#     event = EventSerializer(many=False)
#     class Meta:
#         model = models.ImagePathModel
#         fields = ['image_url', 'event']




class ImgUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImagePathModel
        fields = ['image_url']

class EventSerializer(serializers.ModelSerializer):
    event_image = ImgUrlSerializer(many=True, read_only=True)
    class Meta:
        model = EventModel
        fields = ['event_id', 'type', 'title', 'event_image']
        extra_kwargs = {
            'event_id': {'required': False}
        }