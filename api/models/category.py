from django.db import models
from api.models import Tag
from authentication.models import User


class Category(models.Model):
    name = models.CharField(max_length=400, blank=True, default='')
    tags = models.ManyToManyField(Tag)
    description = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return str(self.name)

    def get_tags(self):
        return ", ".join([t.name for t in self.tags.all()])