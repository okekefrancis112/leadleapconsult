# Generated by Django 2.0 on 2019-06-26 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0024_auto_20190626_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='company',
            field=models.CharField(default='', max_length=550),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='occupation',
            field=models.CharField(default='', max_length=550),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start_course',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 21, 14, 26, 57, 494305)),
        ),
        migrations.AlterField(
            model_name='playerstatistic',
            name='company',
            field=models.CharField(default='', max_length=500),
        ),
    ]
