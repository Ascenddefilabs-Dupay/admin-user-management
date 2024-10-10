from django.db import models
from cloudinary.models import CloudinaryField

    
class CustomUser(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    user_email = models.EmailField(unique=True)
    user_first_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_last_name = models.CharField(max_length=30)
    user_dob = models.DateField()
    user_phone_number = models.BigIntegerField()
    user_country = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_profile_photo = models.FileField(upload_to='profile_photos/', null=True, blank=True)
    user_address_line_1 = models.CharField()
    user_password = models.CharField()
    # last_login=models.DateTimeField()
    user_status=models.BooleanField(default=False)
    user_hold=models.BooleanField(default=False)
    # user_joined_date = models.DateField()
    # user_address_line_2 = models.CharField()
    user_type = models.CharField()
    user_state= models.CharField()
    user_pin_code=models.CharField()
    profile_privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')
    
    class Meta:
        db_table = 'users' 
        managed=False 
class TransactionType(models.Model):
    wallet_id = models.CharField(max_length=255)
    transaction_id = models.CharField(primary_key=True, max_length=255)
    transaction_timestamp = models.DateField()
    transaction_type = models.CharField(max_length=255)
    transaction_amount = models.CharField(max_length=255)
    transaction_status=models.CharField()

    class Meta:
        db_table = 'transaction_table'
        managed = False
class TransactionUser(models.Model):
    wallet_id = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=100, primary_key=True)
    transaction_timestamp = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    user_phone_number = models.BigIntegerField()
    transaction_currency = models.CharField(max_length=3)
    transaction_status=models.CharField()
    
    class Meta:
        db_table = 'transaction_table'
        managed=False


from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class FiatWallet(models.Model):
    fiat_wallet_id = models.CharField(max_length=12, blank=True)  # ID should be unique if necessary
    fiat_wallet_address = models.CharField(max_length=255, blank=True)
    fiat_wallet_type = models.CharField(max_length=50)
    fiat_wallet_currency = models.CharField(max_length=10)
    fiat_wallet_balance = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    fiat_wallet_created_time = models.DateTimeField(auto_now_add=True)
    fiat_wallet_updated_time = models.DateTimeField(auto_now=True)
    fiat_wallet_phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Invalid phone number format."
        )],
        blank=True,
        primary_key=True
    )
    fiat_wallet_email = models.EmailField()
    user_id = models.CharField(max_length=255)
    qr_code = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'fiat_wallet'
        managed = False


class UserCurrency(models.Model):
    id = models.AutoField(primary_key=True)
    wallet_id = models.CharField(max_length=255, unique=False)
    currency_type = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=18, decimal_places=8, default=0)

    def __str__(self):
        return f"{self.wallet_id} - {self.currency_type} - Balance: {self.balance}"
    class Meta:
        db_table = 'user_currencies'
        managed = False


class AdminCMS(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    account_type = models.CharField(max_length=100, null=True, blank=True)
    currency_type = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = 'admincms'
        managed = False