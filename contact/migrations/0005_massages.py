# Generated by Django 4.0 on 2022-01-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contact_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=50)),
                ('User_email', models.CharField(max_length=50)),
                ('User_massage', models.TextField()),
            ],
        ),
    ]
