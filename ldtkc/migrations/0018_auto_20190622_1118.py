# Generated by Django 2.0 on 2019-06-22 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0017_auto_20190425_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='mymailisrequired', max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start_course',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 17, 11, 18, 44, 751608)),
        ),
        migrations.AlterField(
            model_name='onlinevideo',
            name='video',
            field=models.FileField(blank=True, max_length=1000, upload_to='https://storage.googleapis.com/bezop-uploads/media/'),
        ),
    ]