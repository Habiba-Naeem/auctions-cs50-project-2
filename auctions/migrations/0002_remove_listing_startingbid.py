# Generated by Django 3.0.2 on 2020-10-13 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='startingbid',
        ),
    ]