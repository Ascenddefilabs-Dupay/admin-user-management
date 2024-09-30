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
    transaction_id = models.CharField(primary_key=True, max_length=255)
    transaction_timestamp = models.DateField()
    transaction_type = models.CharField(max_length=255)
    transaction_amount = models.CharField(max_length=255)
    transaction_status=models.CharField()

    class Meta:
        db_table = 'transaction_table'
        managed = False
class TransactionUser(models.Model):
    transaction_id = models.CharField(max_length=100, primary_key=True)
    transaction_timestamp = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    user_phone_number = models.BigIntegerField()
    transaction_currency = models.CharField(max_length=3)
    
    class Meta:
        db_table = 'transaction_table'
        managed=False