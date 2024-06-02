from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'earning', EarningModelViewSet)
router.register(r'tax', TaxModelViewSet)


urlpatterns = [
	path('home/', home, name="home"),
	path('api/v1/', include(router.urls), name="api"),
]
