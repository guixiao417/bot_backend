from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from authentication.models import User
from api.models import Category


class Template(models.Model):
    BIDDER_CHOICES = (
        ('cf', 'CF'),
        ('santa', 'Santa'),
        ('ls', 'LS'),
        ('balya', 'Balya'),
        ('cr', 'ChenRi'),
        ('yd', 'YD')
    )
    template = models.TextField(blank=True, default='')
    developer = models.CharField(max_length=400, choices=BIDDER_CHOICES, blank=True, default='')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'templates'

    def show_template (self):
        return format_html(
            '<textarea style="width: 70%; height: 100px;" disabled>{}</textarea>',
            self.template
        )