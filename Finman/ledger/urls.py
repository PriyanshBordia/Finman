from django.urls import path, include
from .views import *
from .router import router


urlpatterns = [
	path('', health, name="health"),
	path('api/v1/', include(router.urls), name="api"),
]
