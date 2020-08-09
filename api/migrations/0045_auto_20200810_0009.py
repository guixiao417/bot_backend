# Generated by Django 2.1.3 on 2020-08-09 16:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20200710_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='job',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='newmessage',
            name='createdAt',
        ),
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 0, 9, 45, 103583, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='newmessage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 16, 9, 45, 113587, tzinfo=utc)),
        ),
    ]