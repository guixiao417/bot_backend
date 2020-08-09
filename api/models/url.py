from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from api.models import Category, Tag
class Url(models.Model):
    BIDDER_CHOICES = (
        ('cf', 'CF'),
        ('santa', 'Santa'),
        ('ls', 'LS'),
        ('balya', 'Balya'),
        ('cr', 'ChenRi'),
        ('yd', 'YD')
    )
    url = models.TextField(blank=True, default='')
    tags = models.ManyToManyField(Tag)
    developer = models.CharField(max_length=400, choices=BIDDER_CHOICES, blank=True, default='')
    class Meta:
        db_table = 'urls'

    def get_tags(self):
        return ", ".join([t.name for t in self.tags.all()])
