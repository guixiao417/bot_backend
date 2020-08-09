from django.db import models
from django.utils import timezone
from api.models import Account

class NewMessage(models.Model):
    account = models.ForeignKey(Account, blank=True, default=1, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now())
    class Meta:
        db_table = 'new_messages'
