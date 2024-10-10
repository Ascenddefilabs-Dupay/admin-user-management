from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser,TransactionUser
from .serializers import CustomUserSerializer,TransactionSerializer
from django.db import IntegrityError
from .models import TransactionType
from .serializers import TransactionTypeSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
import logging
logger = logging.getLogger(__name__)





class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'user_id'
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        
        # Delete related records in currency_converter_fiatwallet
        user.fiat_wallets.all().delete()  # This deletes all related fiat_wallets records

        try:
            # Now delete the user
            response = super().destroy(request, *args, **kwargs)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError as e:
            return Response({'error': 'Integrity error occurred while deleting user.'}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        logging.info(f"Incoming data: {request.data}")

        # Check if user_status is null, true, or false
        logging.info(f"Current user status: {user.user_status}")

        # Parse the 'user_hold' value from the request
        user_hold = request.data.get('user_hold')
        logging.info(f"Parsed 'user_hold' value: {user_hold}")
        
        if isinstance(user_hold, str):
            if user_hold.lower() == "true":
                user.user_hold = True
            elif user_hold.lower() == "false":
                user.user_hold = False
        else:
            user.user_hold = bool(user_hold)

        # Ensure `user_hold` is updated regardless of `user_status`
        logging.info(f"Final 'user_hold' value to be saved: {user.user_hold}")

        # Save changes to the user object
        user.save()
        
        return Response({'status': 'updated successfully'})



class TransactionTypeViewSet(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    lookup_field = 'transaction_id'

class TransactionUserViewSet(viewsets.ModelViewSet):
    queryset = TransactionUser.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'wallet_id'
    def list(self, request, wallet_id=None):
        if wallet_id:
            try:
                transactions = TransactionUser.objects.filter(wallet_id=wallet_id)
                serializer = TransactionSerializer(transactions, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "wallet_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse
from .models import UserCurrency,AdminCMS

def get_fiat_wallet_by_user_id(request, wallet_id):
    print('wallet Id:', wallet_id)
    try:
        # Fetch all fiat wallet details for the given wallet_id
        fiat_wallets = UserCurrency.objects.filter(wallet_id=wallet_id)
        
        # If no records found, return a message
        if not fiat_wallets.exists():
            return JsonResponse({"message": "No fiat wallets found for this wallet ID"}, status=404)

        # Serialize the results into a list of dictionaries
        fiat_wallets_data = []
        for wallet in fiat_wallets:
            fiat_wallets_data.append({
                "id": wallet.id,
                "wallet_id": wallet.wallet_id,
                "currency_type": wallet.currency_type,
                "balance": str(wallet.balance),  # Convert to string if necessary
            })

        # Return the data as a JSON response
        return JsonResponse({"fiat_wallets": fiat_wallets_data}, safe=False, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FiatWallet
from .serializers import FiatWalletSerializer  # Import your serializer

class WalletView(APIView):
    def get(self, request, user_id):
        try:
            wallet = FiatWallet.objects.get(user_id=user_id)
            serializer = FiatWalletSerializer(wallet)  # Use the serializer
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FiatWallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
def get_currency_icon_by_currency_type(request, currency_type):
    try:
        # Fetch the icon details based on currency_type from AdminCMS
        currency_icons = AdminCMS.objects.filter(currency_type=currency_type)
        print('Currency Type:', currency_type)
        
        # Check if the record exists
        if not currency_icons.exists():
            # Return default icon URL if no currency icons are found
            return JsonResponse({
                "currency_icons": [
                    {
                        "account_type": None,
                        "currency_type": currency_type,
                        "icon": "image/upload/v1727948965/61103_ttcaan.png"
                    }
                ]
            }, safe=False, status=200)

        # Prepare the response data
        currency_icons_data = [
            {
                "account_type": icon.account_type,
                "currency_type": icon.currency_type,
                "icon": icon.icon,
            }
            for icon in currency_icons
        ]

        # Return the icons as a JSON response
        return JsonResponse({"currency_icons": currency_icons_data}, safe=False, status=200)

    except Exception as e:
        # Handle any unexpected errors
        return JsonResponse({"error": str(e)}, status=500)