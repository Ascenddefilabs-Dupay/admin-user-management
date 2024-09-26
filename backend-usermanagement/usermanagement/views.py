from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser,WalletAdminActions,TransactionUser
from .serializers import CustomUserSerializer,WalletAdminActionsSerializer,TransactionSerializer
from django.db import IntegrityError
from rest_framework.decorators import action  # Make sure this import is present
from .models import TransactionType
from .serializers import TransactionTypeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser,AdminUser,Customer
from .serializers import CustomUserSerializer,AdminUserSerializer
import logging
logger = logging.getLogger(__name__)
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Count # type: ignore
from django.utils.timezone import now, timedelta # type: ignore
from django.http import JsonResponse # type: ignore


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    lookup_field = 'user_id'

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


@api_view(['POST'])
def create_user(request):
    logger.info(request.data)  # Log the incoming data
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletAdminActionsViewSet(viewsets.ModelViewSet):
    queryset = WalletAdminActions.objects.all()  # Retrieve all records
    serializer_class = WalletAdminActionsSerializer
    lookup_field = 'id'

    # Override the create method if custom behavior is needed
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Override the update method if custom behavior is needed
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # Override the destroy method for custom deletion behavior
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Add custom filtering or querying logic if necessary
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
class TransactionTypeViewSet(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    lookup_field = 'transaction_id'

class TransactionUserViewSet(viewsets.ModelViewSet):
    queryset = TransactionUser.objects.all()
    serializer_class = TransactionSerializer
def get_user_registration_stats(request):
    # Daily registered users (last 6 days)
        daily_counts = Customer.objects.filter(
            user_joined_date__gte=now() - timedelta(days=6)
        ).extra(select={'day': 'date(user_joined_date)'}).values('day').annotate(count=Count('user_id'))

        # Monthly registered users (last 6 months)
        monthly_counts = Customer.objects.filter(
            user_joined_date__gte=now() - timedelta(days=180)
        ).extra(select={'month': "to_char(user_joined_date, 'YYYY-MM')"}).values('month').annotate(count=Count('user_id'))

        return JsonResponse({
            'daily': list(daily_counts),
            'monthly': list(monthly_counts),
        })