# Generated by Django 2.1.3 on 2020-06-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='router',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]
