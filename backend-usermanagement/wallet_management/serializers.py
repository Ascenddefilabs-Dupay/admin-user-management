from rest_framework import serializers
from .models import UserCurrency



class UserCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCurrency
        fields = '__all__'