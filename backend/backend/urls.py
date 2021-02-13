from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pills import views
# from rest_framework.authtoken import views as authviews


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'pills',views.PillsViewSet)
# router.register(r'schedule', views.ScheduleViewSet)
# router.register(r'medical', views.MedicalViewSet)
# router.register(r'plans', views.PlansViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('test/',include('ambee.urls')),
    
    # path('authentication/', include('authentication.urls', namespace='authentication')),
    # path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
]


