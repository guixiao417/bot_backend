from django.db import models
from django.utils import timezone
from django.utils.html import format_html

class Tag(models.Model):
    name = models.CharField(max_length=400, blank=True, default='')
    class Meta:
        db_table = 'tags'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return str(self.name)