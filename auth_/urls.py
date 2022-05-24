from django.urls import path

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
]

router = routers.SimpleRouter()
router.register(r'', views.AuthenticationViewSet, basename='authentication')
urlpatterns.extend(router.urls)
