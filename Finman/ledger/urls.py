from django.urls import path, include
from .views import *
from .router import router


urlpatterns = [
	path('home/', home, name="home"),
	path('api/v1/', include(router.urls), name="api"),
]
