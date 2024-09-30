from django.shortcuts import render
from rest_framework import viewsets
from .models import AdminUser
from .serializers import AdminUserSerializer
import logging
logger = logging.getLogger(__name__)

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    lookup_field = 'user_id'
