# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CustomUserViewSet,get_fiat_wallet_by_user_id
# from .views import TransactionUserViewSet,WalletView

# router = DefaultRouter()
# router.register(r'profile', CustomUserViewSet, basename="myProfile")
# router.register(r'transaction',TransactionUserViewSet,basename="transaction")

# urlpatterns = [
#     path('', include(router.urls)),
#     path('fiat_wallet/<str:wallet_id>/', get_fiat_wallet_by_user_id, name='get_fiat_wallet_by_user_id'),
#       path('fiat_wallet/<str:user_id>/', WalletView.as_view(), name='fiat_wallet'),

# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet,get_fiat_wallet_by_user_id,get_currency_icon_by_currency_type
from .views import TransactionUserViewSet,WalletView


router = DefaultRouter()
router.register(r'profile', CustomUserViewSet, basename="myProfile")
router.register(r'transaction',TransactionUserViewSet,basename="transaction")

urlpatterns = [
    path('', include(router.urls)),
    path('transactions/<str:wallet_id>/', TransactionUserViewSet.as_view({'get': 'list'}), name='transaction-list'),
    # path('fiat_wallet/<str:wallet_id>/', get_fiat_wallet_by_user_id, name='get_fiat_wallet_by_user_id'),
    path('fiat_wallet/<str:wallet_id>/', get_fiat_wallet_by_user_id, name='get_fiat_wallet_by_user_id'),
    # path('wallets/<int:fiat_wallet_id>/', get_user_id_and_balance_by_wallet_id, name='get_wallet_info'),
    path('fiat_wallets/<str:user_id>/', WalletView.as_view(), name='fiat_wallet'),
    path('currency-icons/<str:currency_type>/', get_currency_icon_by_currency_type, name='get_currency_icon_by_currency_type'),
]