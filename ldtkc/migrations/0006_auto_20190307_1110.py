# Generated by Django 2.0 on 2019-03-07 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0005_resources_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resources',
            old_name='image',
            new_name='resource',
        ),
    ]