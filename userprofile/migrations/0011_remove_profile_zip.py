# Generated by Django 4.0 on 2022-01-23 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Zip',
        ),
    ]
