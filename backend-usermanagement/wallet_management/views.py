from django.shortcuts import render
from rest_framework import viewsets
from .models import UserCurrency
from .serializers import UserCurrencySerializer
import logging
logger = logging.getLogger(__name__)





class UserCurrencyViewSet(viewsets.ModelViewSet):
    queryset = UserCurrency.objects.all()
    serializer_class = UserCurrencySerializer
    lookup_field = 'user_id'