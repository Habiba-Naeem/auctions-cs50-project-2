# Generated by Django 3.0.2 on 2020-10-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_watchlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bid',
        ),
    ]