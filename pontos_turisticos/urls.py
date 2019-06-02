from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PontosTuristicosViewSet

router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontosTuristicosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
