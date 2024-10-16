# from django.db import models
# from cloudinary.models import CloudinaryField
# from django.contrib.auth.hashers import make_password, check_password


# class AdminUser(models.Model):
#     user_id = models.CharField(max_length=8, primary_key=True)
#     user_email = models.EmailField(unique=True)
#     user_first_name = models.CharField(max_length=30)
#     user_middle_name = models.CharField(max_length=30, blank=True)
#     user_last_name = models.CharField(max_length=30)
#     user_dob = models.DateField()
#     user_phone_number = models.BigIntegerField()
#     user_password = models.CharField(max_length=128)
#     # last_login=models.DateTimeField()
#     user_status=models.BooleanField(default=False)
#     user_hold=models.BooleanField(default=False)
#     # user_joined_date = models.DateField()
#     # user_address_line_2 = models.CharField()
#     user_type = models.CharField()
#     profile_privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')
#     def save(self, *args, **kwargs):
#         # Ensure that the password is hashed with PBKDF2 if it's not already in the correct format
#         if not self.pk or not self.user_password.startswith('pbkdf2_sha256$'):
#             self.user_password = make_password(self.user_password)

#         # Call the save method of the parent class
#         super().save(*args, **kwargs)

#     def check_password(self, raw_password):
#         # Check if the raw_password matches the hashed password in the database
#         return check_password(raw_password, self.user_password)
#     class Meta:
#         db_table = 'users' 
#         managed=False
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.hashers import make_password, check_password

class AdminUser(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    user_email = models.EmailField(unique=True)
    user_first_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_last_name = models.CharField(max_length=30)
    user_dob = models.DateField()
    user_phone_number = models.BigIntegerField()
    user_password = models.CharField(max_length=128)
    user_status = models.BooleanField(default=False)
    user_hold = models.BooleanField(default=False)
    user_type = models.CharField(max_length=30)
    profile_privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')

    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if not self.pk or not self.user_password.startswith('pbkdf2_sha256$'):
            self.user_password = make_password(self.user_password)

        # Call the save method of the parent class
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the raw_password matches the hashed password in the database
        return check_password(raw_password, self.user_password)

    class Meta:
        db_table = 'users'
        managed = False
