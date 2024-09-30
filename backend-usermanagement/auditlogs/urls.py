from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletAdminActionsViewSet

router = DefaultRouter()
router.register(r'wallet-admin-actions', WalletAdminActionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
