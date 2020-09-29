from django.db import models
from django.utils import timezone
from api.models import Job, Template
from authentication.models import User


class Bid(models.Model):
    job = models.ForeignKey(Job, blank=True, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, blank=True, default=None, on_delete=models.CASCADE)
    bot = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'bids'
        
