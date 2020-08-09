# Generated by Django 2.1.3 on 2020-06-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200628_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=400)),
                ('template', models.TextField(blank=True, default='')),
                ('developer', models.CharField(blank=True, choices=[('cf', 'CF'), ('santa', 'Santa'), ('ls', 'LS'), ('balya', 'Balya'), ('cr', 'ChenRi'), ('yd', 'YD')], default='', max_length=400)),
            ],
            options={
                'db_table': 'templates',
            },
        ),
    ]
