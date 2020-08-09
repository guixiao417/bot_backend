from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from api.models import Category, Account
class Template(models.Model):
    BIDDER_CHOICES = (
        ('cf', 'CF'),
        ('santa', 'Santa'),
        ('ls', 'LS'),
        ('balya', 'Balya'),
        ('cr', 'ChenRi'),
        ('yd', 'YD')
    )
    account = models.ForeignKey(Account, blank=True, default=1, on_delete=models.CASCADE)
    template = models.TextField(blank=True, default='')
    developer = models.CharField(max_length=400, choices=BIDDER_CHOICES, blank=True, default='')
    class Meta:
        db_table = 'templates'
    def show_template (self):
        return format_html(
            '<textarea style="width: 70%; height: 100px;" disabled>{}</textarea>',
            self.template
        )