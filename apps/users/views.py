from django.core import paginator
from django.db import models
from django.db.models import query
from rest_framework import generics, status, permissions
from rest_framework import response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from apps.users.models import ClientModel, UsersModel
from apps.users.serializers.user_serializers import ClientListSerialize, ClientSerialize, UserListSerializer, UserSerializer
from commons.custom_exception import ExceptionMiddleware
from commons.custom_pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException
from commons.permission import CustomPermission


# class UserViewSet(generics.ListAPIView):
#     queryset = UsersModel.objects.all()
#     serializer_class = UserSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['last_name_kanji', 'first_name_kanji']


# class UserViewSet(APIView):
#     def get(self, request,*args,**kwargs):
#         last_name_kanji = request.GET.get('last_name_kanji') or ''
#         first_name_kanji = request.GET.get('first_name_kanji') or ''
#         users = UsersModel.objects.filter(last_name_kanji__icontains=last_name_kanji, first_name_kanji__icontains=first_name_kanji)
#         paginator = CustomPagination()
#         result_page = paginator.paginate_queryset(users,request)
#         serializer = UserSerializer(result_page,many=True)
#         return paginator.get_paginated_response(serializer.data)

    
class UserViewSet(generics.ListAPIView):
    queryset = UsersModel.objects
    pagination_class = CustomPagination
    # serializer_class = UserListSerializer
    

    def get(self, request, *args, **kwargs):
        # last_name_kanji = request.GET.get('last_name_kanji') or ''
        # first_name_kanji = request.GET.get('first_name_kanji') or ''
        # users = UsersModel.objects.select_related('client').filter(last_name_kanji__icontains=last_name_kanji, first_name_kanji__icontains=first_name_kanji)
        
        users = UsersModel.objects.all().select_related('client')
        serializer = UserListSerializer(users, many=True)
        result = self.paginate_queryset(serializer.data)

        return self.get_paginated_response(result)



# class UserViewSet(generics.ListAPIView):
#     queryset = ClientModel.objects
#     pagination_class = CustomPagination
    

#     def get(self, request, *args, **kwargs):
        
#         users = ClientModel.objects.all().select_related('client')
#         serializer = ClientListSerialize(users, many=True)
#         result = self.paginate_queryset(serializer.data)

#         return self.get_paginated_response(result)



# class UserDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = UsersModel.objects.filter(is_deleted=False)
#     serializer_class = UserSerializer
