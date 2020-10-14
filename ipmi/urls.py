from django.urls import include, path
# from rest_framework import routers
from . import views
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path("devices/",views.get_all_devices,name='devices'),
    path('scan/', views.scan_devices, name='scan'),
    path('credentials/', views.update_credentials, name='credentials'),
    path('powerctl/', views.powerctl, name='powerctl'),
    path('powerctl_patch/', views.powerctl_patch, name='powerctl_patch'),
    path('power_status/', views.power_status, name='power_status'),
    path('<str:ip>/temperature/',views.get_device_temperature,name="temperature")
]
