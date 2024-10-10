from rest_framework import serializers
from .models import CustomUser
from datetime import datetime
from .models import TransactionType,TransactionUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TransactionTypeSerializer(serializers.ModelSerializer):
    transaction_timestamp = serializers.SerializerMethodField()
    class Meta:
        model = TransactionType
        fields = '__all__'
    def get_transaction_timestamp(self, obj):
        # Convert datetime to date
        if isinstance(obj.transaction_timestamp, datetime):
            return obj.transaction_timestamp.date()
        return obj.transaction_timestamp
class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = TransactionUser
        fields = '__all__'
    def get_user(self, obj):
        users = CustomUser.objects.filter(user_phone_number=obj.user_phone_number)
        if users.exists():
            # If there are multiple users, you need to decide how to handle it
            # For example, return the first user or handle it according to your requirements
            user = users.first()  # Get the first user from the queryset
            return {
                # 'user_id': user.user_id,
                # 'user_first_name': user.user_first_name,
                'user_phone_number': user.user_phone_number,
                # 'user_profile_photo': user.user_profile_photo,
            }
        return None
# transactions/serializers.py

from rest_framework import serializers
from .models import FiatWallet

class FiatWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiatWallet
        fields = '__all__'  # Specify the fields you want to serialize
