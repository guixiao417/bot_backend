from django.db import models
from django.utils import timezone
from authentication.models import User


class NewMessage(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    class Meta:
        db_table = 'new_messages'
