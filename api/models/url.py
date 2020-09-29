from django.db import models
from api.models import Tag
from authentication.models import User


class Url(models.Model):
    BIDDER_CHOICES = (
        ('cf', 'CF'),
        ('santa', 'Santa'),
        ('ls', 'LS'),
        ('balya', 'Balya'),
        ('cr', 'ChenRi'),
        ('yd', 'YD')
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    url = models.TextField(blank=True, default='')
    tags = models.ManyToManyField(Tag)
    developer = models.CharField(max_length=400, choices=BIDDER_CHOICES, blank=True, default='')

    class Meta:
        db_table = 'urls'

    def get_tags(self):
        return ", ".join([t.name for t in self.tags.all()])
