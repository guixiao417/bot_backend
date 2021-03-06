from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.timezone import timedelta
from api.models import Category
from authentication.models import User


class Job(models.Model):
    title = models.CharField(max_length=400, blank=True, default='')
    hourly = models.BooleanField(default=False)
    currency = models.CharField(max_length=400, blank=True, default='')
    budget = models.CharField(max_length=400, blank=True, default='')
    maxBudget = models.FloatField(blank=True, default=0)
    skills = models.CharField(max_length=400, blank=True, default='')
    country = models.CharField(max_length=400, blank=True, default='')
    completedJob = models.IntegerField(default=0) 
    memberDate = models.DateTimeField(default=timezone.now)
    projectId = models.CharField(max_length=400, blank=True, default='')
    v_identity = models.BooleanField(default=False)
    v_payment = models.BooleanField(default=False)
    v_deposit = models.BooleanField(default=False)
    v_email = models.BooleanField(default=False)
    v_profile = models.BooleanField(default=False)
    v_phone = models.BooleanField(default=False)
    count = models.IntegerField(default=1)
    router = models.CharField(max_length=400, blank=True, default='')
    recruiter = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    check_status = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, null=True, blank=True)
    bidder = models.ManyToManyField(User, blank=True, null=True, related_name="bidders")
    rate = models.FloatField(default=0)
    status = models.CharField(max_length=400, blank=True, null=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'jobs'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return str(self.title)

    def view_job (self):
        return format_html(
            '<a href="{}" target="new">view job</a>',
            self.router,
        )
    def title_view (self):
        return format_html(
            '<a href="{}" target="new">{}({})</a>',
            self.router, self.title, self.skills
        )

    def sent_proposal(self):
        return ", ".join([b.username for b in self.bidder.all()])

    def read_by_bot(self):
        return ", ".join([b.name for b in self.bot.all()])

    def time_before(self):
        time_now = timezone.now()
        time_delta = time_now - self.created_at
        return time_delta

    def view_category(self):
        categories = self.category.all()
        category_name = ''
        for category in categories:
            if category.user:
                category_name += "%s-%s\n" % (category.user.username, category.name)
            else:
                category_name += "None-%s\n" % category.name
        return category_name