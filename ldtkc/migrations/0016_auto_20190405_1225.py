# Generated by Django 2.0 on 2019-04-05 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0015_auto_20190405_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='start_course',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 12, 25, 19, 17093)),
        ),
        migrations.AlterField(
            model_name='onlineclass',
            name='slug',
            field=models.SlugField(default='', max_length=1500),
        ),
    ]
