# Generated by Django 4.0 on 2021-12-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
