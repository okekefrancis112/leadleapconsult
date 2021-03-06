# Generated by Django 3.0 on 2021-12-23 12:44

import cloudinary_storage.storage
import cloudinary_storage.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0027_auto_20190628_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_test_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registeration',
            name='is_test_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.FileField(blank=True, max_length=1000, upload_to='course_image/'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='outline',
            field=models.FileField(blank=True, max_length=10000, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='course_file/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery_image/'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start_course',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 12, 44, 3, 707800)),
        ),
        migrations.AlterField(
            model_name='onlinevideo',
            name='video',
            field=models.FileField(blank=True, max_length=1000, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='online_video/', validators=[cloudinary_storage.validators.validate_video]),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='pick_your_course',
            field=models.CharField(default='Pick a Course', max_length=100),
        ),
        migrations.AlterField(
            model_name='resources',
            name='resource',
            field=models.FileField(blank=True, max_length=1000, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='resource/'),
        ),
        migrations.AlterField(
            model_name='satisfiedclient',
            name='image',
            field=models.ImageField(blank=True, upload_to='satisfied_client/'),
        ),
    ]
