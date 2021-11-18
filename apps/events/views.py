from django.core import paginator
from django.db import models
from django.db.models.query import Prefetch
from rest_framework import generics, status, permissions
from rest_framework import response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from apps.events.models import EventModel
from apps.events.serializers.event_serializers import EventSerializer, ImgUrlSerializer

from apps.users.models import ImagePathModel, UsersModel
from apps.users.serializers.user_serializers import UserSerializer
from commons.custom_exception import ExceptionMiddleware
from commons.custom_pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException


class EventViewSet(generics.ListAPIView):
    queryset = EventModel.objects
    pagination_class = CustomPagination
    

    def get(self, request, *args, **kwargs):
        type = request.GET.get('type', '')
        keyword = request.GET.get('keyword') or ''
        
        events = EventModel.objects.prefetch_related('event_image', 'eauu').filter(type__contains=type, title__icontains=keyword)
        serializer = EventSerializer(events, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


