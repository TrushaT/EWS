from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pills import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('test/',include('ambee.urls')),
]
