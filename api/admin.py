import json
import datetime
from datetime import timedelta
from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from api import models
from api.serializers import JobSerializer
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncDate
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.utils import timezone
import pytz

# Register your models here.
def make_checked(modeladmin, request, queryset):
    queryset.update(checked=True)
    make_checked.short_description = "Make selected job"

# Register your models here.
def make_disabled(modeladmin, request, queryset):
    queryset.update(disabled=True)
    make_disabled.short_description = "Make disable job"

class JobLevelFilter(SimpleListFilter):
    title = 'Job Level Filter' # a label for our filter
    parameter_name = 'pages'
    def lookups(self, request, model_admin):
        # This is where you create filter options; we have two:
        return [
            ('low', 'Fixed less than 1000 USD'),
            ('high', 'Hourly, Fixed more than 1000 USD')
        ]

    def queryset(self, request, queryset):
        # This is where you process parameters selected by use via filter options:
        if self.value() == 'low':
            return queryset.filter(hourly=False, maxBudget__lt=1000.0)
        elif self.value() == 'high':
            return queryset.exclude(hourly=False, maxBudget__lt=1000.0)
        else:
            return queryset

class DateFilter(SimpleListFilter):
    title = 'Date Filter' # a label for our filter
    parameter_name = 'duration'
    def lookups(self, request, model_admin):
        # This is where you create filter options; we have two:
        return [
            ('day', 'A Day'),
            ('week', 'A Week'),
            ('week_ago', 'A Week ago'),
            ('month', 'A Month'),
        ]

    def queryset(self, request, queryset):
        # This is where you process parameters selected by use via filter options:
        if self.value() == 'day':
            return queryset.filter(created_at__gte=datetime.datetime.now() - timedelta(days=1))
        elif self.value() == 'week':
            return queryset.filter(created_at__gte=datetime.datetime.now() - timedelta(days=6))
        elif self.value() == 'week_ago':
            return queryset.filter(created_at__lte=datetime.datetime.now() - timedelta(days=8))
        elif self.value() == 'month':
            return queryset.filter(created_at__gte=datetime.datetime.now() - timedelta(days=30))
        else:
            return queryset

@admin.register(models.Job)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_view', 'hourly', 'currency', 'budget', 'country', 'completedJob', 'memberDate', 'v_payment', 'v_deposit', 'time_before', 'created_at', 'sent_proposal', 'read_by_bot', 'status', 'check_status')
    actions = [make_checked, make_disabled,]
    list_filter = (JobLevelFilter, DateFilter, 'status', 'check_status')
    search_fields = ('title', 'skills', )

    def changelist_view(self, request, extra_context=None):
        if 'pages' in request.GET:
            if request.GET['pages'] =='high':
                chart_data = models.Job.objects.exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                chart_data_accept = models.Job.objects.filter(status="Accepted").exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                chart_data_complete = models.Job.objects.filter(status="Complete").exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                #
                # chart_data1 = models.Job.objects.exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                # chart_data1_accept = models.Job.objects.filter(status="Accepted").exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                # chart_data1_complete = models.Job.objects.filter(status="Complete").exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                #
                # chart_data2 = models.Job.objects.filter(bot=account).exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                # chart_data3 = models.Job.objects.exclude(hourly=False, maxBudget__lt=1000.0).extra({'date': 'country'}).values("date").annotate(y=Count("id"))
            else:
                chart_data = models.Job.objects.filter(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                chart_data_accept = models.Job.objects.filter(hourly=False, maxBudget__lt=1000.0, status="Accepted").extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                chart_data_complete = models.Job.objects.filter(hourly=False, maxBudget__lt=1000.0, status="Complete").extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                #
                # chart_data1 = models.Job.objects.filter(hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                # chart_data1_accept = models.Job.objects.filter(status="Accepted", hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                # chart_data1_complete = models.Job.objects.filter(status="Complete", hourly=False, maxBudget__lt=1000.0).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                #
                # chart_data2 = models.Job.objects.filter(hourly=False, maxBudget__lt=1000.0).filter(bot=account).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
                # chart_data3 = models.Job.objects.filter(hourly=False, maxBudget__lt=1000.0).extra({'date': 'country'}).values("date").annotate(y=Count("id"))
        else:
            chart_data = models.Job.objects.extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            chart_data_accept = models.Job.objects.filter(status="Accepted").extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            chart_data_complete = models.Job.objects.filter(status="Complete").extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            #
            # chart_data1 = models.Job.objects.extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            # chart_data1_accept = models.Job.objects.filter(status="Accepted").extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            # chart_data1_complete = models.Job.objects.filter(status="Complete").extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            #
            # chart_data2 = models.Job.objects.filter(bot=account).extra({'date': 'date(created_at)'}).values("date").annotate(y=Count("id"))
            # chart_data3 = models.Job.objects.extra({'date': 'country'}).values("date").annotate(y=Count("id"))
        
        if 'country' in request.GET:
            chart_data = chart_data.filter(country=request.GET['country'])
            chart_data_accept = chart_data_accept.filter(country=request.GET['country'])
            chart_data_complete = chart_data_complete.filter(country=request.GET['country'])
            #
            # chart_data1 = chart_data1.filter(country=request.GET['country'])
            # chart_data1_accept = chart_data1_accept.filter(status="Accepted", country=request.GET['country'])
            # chart_data1_complete = chart_data1_complete.filter(status="Complete", country=request.GET['country'])
            #
            # chart_data2 = chart_data2.filter(country=request.GET['country'])
            # chart_data3 = chart_data3.filter(country=request.GET['country'])

        if 'status' in request.GET:
            chart_data = chart_data.filter(status=request.GET['status'])
            chart_data_accept = chart_data_accept.filter(status=request.GET['status'])
            chart_data_complete = chart_data_complete.filter(status=request.GET['status'])
            #
            # chart_data1 = chart_data1.filter(status=request.GET['status'])
            # chart_data1_accept = chart_data1_accept.filter(status=request.GET['status'])
            # chart_data1_complete = chart_data1_complete.filter(status=request.GET['status'])
            #
            # chart_data2 = chart_data2.filter(status=request.GET['status'])
            # chart_data3 = chart_data3.filter(status=request.GET['status'])
        
        if 'duration' in request.GET:
            if request.GET['duration'] == 'week_ago':
                days = 8
                chart_data = chart_data.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                chart_data_accept = chart_data_accept.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                chart_data_complete = chart_data_complete.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                #
                # chart_data1 = chart_data1.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                # chart_data1_accept = chart_data1_accept.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                # chart_data1_complete = chart_data1_complete.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                #
                # chart_data2 = chart_data2.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                # chart_data3 = chart_data3.filter(created_at__lte=datetime.datetime.now() - timedelta(days=days))
                
            else:
                days = 1
                if request.GET['duration'] == 'day':
                    days = 1
                elif request.GET['duration'] == 'week':
                    days = 7
                elif request.GET['duration'] == 'month':
                    days = 31
                chart_data = chart_data.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                chart_data_accept = chart_data_accept.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                chart_data_complete = chart_data_complete.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                
                # chart_data1 = chart_data1.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                # chart_data1_accept = chart_data1_accept.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                # chart_data1_complete = chart_data1_complete.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                #
                # chart_data2 = chart_data2.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                # chart_data3 = chart_data3.filter(created_at__gte=datetime.datetime.now() - timedelta(days=days))
                

        chart_data = (chart_data.order_by("-date"))
        chart_data_accept = (chart_data_accept.order_by("-date"))
        chart_data_complete = (chart_data_complete.order_by("-date"))

        # chart_data1 = (chart_data1.order_by("-date"))
        # chart_data1_accept = (chart_data1_accept.order_by("-date"))
        # chart_data1_complete = (chart_data1_complete.order_by("-date"))
        #
        # chart_data2 = (chart_data2.order_by("-date"))
        # chart_data3 = (chart_data3.order_by("-date"))

        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        as_accept_json = json.dumps(list(chart_data_accept), cls=DjangoJSONEncoder)
        as_complete_json = json.dumps(list(chart_data_complete), cls=DjangoJSONEncoder)

        # as_json1 = json.dumps(list(chart_data1), cls=DjangoJSONEncoder)
        # as_accept_json1 = json.dumps(list(chart_data1_accept), cls=DjangoJSONEncoder)
        # as_complete_json1 = json.dumps(list(chart_data1_complete), cls=DjangoJSONEncoder)
        #
        # as_json2 = json.dumps(list(chart_data2), cls=DjangoJSONEncoder)
        # as_json3 = json.dumps(list(chart_data3), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json, "chart_data_accept": as_accept_json, \
        "chart_data_complete": as_complete_json}
        extra_context = extra_context
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(models.Category)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_tags', 'description')


@admin.register(models.Template)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'show_template', 'developer')

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(models.Filter)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'notification', 'description', 'private_key', 'fixed_budget', 'hourly_budget', 'payment_filter', 'time_delta', 'job_count', 'filter_countries')
    filter_horizontal = ('countries',)


@admin.register(models.Url)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'get_tags', 'developer')
    filter_horizontal = ('tags',)

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(models.Bid)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id',  'job', 'template', 'bot', 'created_at')

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(models.Tag)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Country)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.NewMessage)
class InviteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'checked', 'created_at')

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)