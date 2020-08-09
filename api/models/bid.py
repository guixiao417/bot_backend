from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from api.models import Job, Account, Category, Template

class Bid(models.Model):
    job = models.ForeignKey(Job, blank=True, default=None, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, blank=True, default=None, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, blank=True, default=None, on_delete=models.CASCADE)
    bot = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'bids'
        
