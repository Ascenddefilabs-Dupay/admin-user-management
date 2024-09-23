from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet,WalletAdminActionsViewSet,TransactionTypeViewSet
from .views import TransactionUserViewSet

router = DefaultRouter()
router.register(r'profile', CustomUserViewSet, basename="myProfile")
router.register(r'wallet-admin-actions', WalletAdminActionsViewSet)
router.register(r'transactions', TransactionTypeViewSet)
router.register(r'transaction',TransactionUserViewSet,basename="transaction")

urlpatterns = [
    path('', include(router.urls)),
]
