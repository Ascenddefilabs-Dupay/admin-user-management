from django.shortcuts import render
from rest_framework import viewsets
from .models import WalletAdminActions
from .serializers import WalletAdminActionsSerializer
from django.db import IntegrityError
from rest_framework.decorators import action  # Make sure this import is present
from rest_framework import status
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)



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
