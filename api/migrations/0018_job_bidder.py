# Generated by Django 2.1.3 on 2020-06-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_bid_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='bidder',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]
