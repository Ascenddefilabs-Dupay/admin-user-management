from rest_framework import serializers
from .models import WalletAdminActions
from datetime import datetime


class WalletAdminActionsSerializer(serializers.ModelSerializer):
    admins_actions_date = serializers.SerializerMethodField()
    class Meta:
        model = WalletAdminActions
        fields = ['admins_actions_date', 'admins_actions_username', 'admins_actions', 'admins_actions_name', 'admin_email']
    def get_admins_actions_date(self, obj):
        # Check if the field is datetime and convert it to date
        if isinstance(obj.admins_actions_date, datetime):
            return obj.admins_actions_date.date()
        return obj.admins_actions_date
