from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCurrencyViewSet

router = DefaultRouter()
router.register(r'profile', UserCurrencyViewSet, basename="myProfile")

urlpatterns = [
    path('', include(router.urls)),
]