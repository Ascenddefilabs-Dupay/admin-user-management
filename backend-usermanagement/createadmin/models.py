from django.db import models
from cloudinary.models import CloudinaryField


class AdminUser(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    user_email = models.EmailField(unique=True)
    user_first_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_last_name = models.CharField(max_length=30)
    user_dob = models.DateField()
    user_phone_number = models.BigIntegerField()
    user_password = models.CharField()
    # last_login=models.DateTimeField()
    user_status=models.BooleanField(default=False)
    user_hold=models.BooleanField(default=False)
    # user_joined_date = models.DateField()
    # user_address_line_2 = models.CharField()
    user_type = models.CharField()
    profile_privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')
    
    class Meta:
        db_table = 'users' 
        managed=False
