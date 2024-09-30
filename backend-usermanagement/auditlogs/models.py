from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone

class WalletAdminActions(models.Model):
    id=models.CharField(primary_key=True)
    admins_actions_date=models.DateField(default=timezone.now)
    admins_actions_username=models.CharField()
    admins_actions=models.CharField()
    admins_actions_name=models.CharField()
    admin_email=models.CharField(unique=True)

    class Meta:
        db_table = 'wallet_admins_actions'
        managed = False  
