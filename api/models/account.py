import uuid
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from api.models import Country

class Account(models.Model):
    name = models.CharField(max_length=400, blank=True, default='')
    description = models.TextField(blank=True, default='')
    private_key = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False) 
    fixed_budget = models.IntegerField(blank=True, null=True, default=750)
    hourly_budget = models.IntegerField(blank=True, null=True, default=20)
    payment_filter = models.BooleanField(default=True)
    time_delta = models.IntegerField(blank=True, null=True, default=30)
    job_count = models.IntegerField(blank=True, null=True, default=10)
    countries = models.ManyToManyField(Country)
    notification = models.BooleanField(default=False)

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return str(self.name)

    def filter_countries(self):
        return ", ".join([t.name for t in self.countries.all()])