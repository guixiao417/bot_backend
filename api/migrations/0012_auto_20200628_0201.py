# Generated by Django 2.1.3 on 2020-06-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='name',
        ),
        migrations.AddField(
            model_name='template',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]
