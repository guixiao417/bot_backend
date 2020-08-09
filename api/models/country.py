from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=400, blank=True, default='')
    class Meta:
        db_table = 'countries'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return str(self.name)
