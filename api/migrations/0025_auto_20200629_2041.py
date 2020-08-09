# Generated by Django 2.1.3 on 2020-06-29 12:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200629_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
        migrations.AlterField(
            model_name='job',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 20, 41, 41, 174960, tzinfo=utc)),
        ),
    ]
