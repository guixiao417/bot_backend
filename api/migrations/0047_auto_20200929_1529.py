# Generated by Django 2.1.3 on 2020-09-29 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0046_auto_20200929_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 15, 29, 46, 241586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newmessage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 7, 29, 46, 250583, tzinfo=utc)),
        ),
    ]
