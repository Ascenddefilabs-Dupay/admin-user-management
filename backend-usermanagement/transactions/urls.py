from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet
from .views import TransactionUserViewSet

router = DefaultRouter()
router.register(r'profile', CustomUserViewSet, basename="myProfile")
router.register(r'transaction',TransactionUserViewSet,basename="transaction")

urlpatterns = [
    path('', include(router.urls)),
]
