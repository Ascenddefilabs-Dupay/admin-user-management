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
