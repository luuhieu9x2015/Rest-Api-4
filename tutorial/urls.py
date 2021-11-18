from django.contrib import admin
import debug_toolbar
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('apps.users.urls')),
    path('api/v1', include('apps.events.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
