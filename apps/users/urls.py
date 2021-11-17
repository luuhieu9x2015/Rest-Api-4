from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token




# router = DefaultRouter()
# # router.register('', views.UserViewSet, basename='user')
# router.register(r'', views.UserViewSet, basename='user')


urlpatterns = [
    path('/users', views.UserViewSet.as_view(), name='user_list'),
    path('/login', obtain_jwt_token),
    path('/refresh-token', refresh_jwt_token),

    # path('', include(router.urls))
#     url(r'^/users$', UserListCreateAPIView.as_view(), name='user_list'),
#     path('/user/<int:pk>', UserDetailUpdateAPIView.as_view(), name='user_detail_update'),
]