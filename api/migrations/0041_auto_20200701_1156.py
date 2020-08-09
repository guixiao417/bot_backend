# Generated by Django 2.1.3 on 2020-07-01 03:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20200701_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 11, 56, 8, 570359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newmessage',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 3, 56, 8, 575346, tzinfo=utc)),
        ),
    ]
