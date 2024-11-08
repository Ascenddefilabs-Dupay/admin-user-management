from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet,WalletAdminActionsViewSet,TransactionTypeViewSet,AdminUserViewSet
from .views import TransactionUserViewSet,get_user_registration_stats

router = DefaultRouter()
router.register(r'profile', CustomUserViewSet, basename="myProfile")
router.register(r'wallet-admin-actions', WalletAdminActionsViewSet)
router.register(r'transactions', TransactionTypeViewSet)
router.register(r'AdminUser', AdminUserViewSet)
router.register(r'transaction',TransactionUserViewSet,basename="transaction")

urlpatterns = [
    path('', include(router.urls)),
    path('user-registration-stats/', get_user_registration_stats, name='user-registration-stats'),
]
