# Generated by Django 4.0 on 2022-01-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_massages'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Massages',
        ),
    ]
