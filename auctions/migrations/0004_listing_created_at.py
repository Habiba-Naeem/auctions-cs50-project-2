# Generated by Django 3.0.2 on 2020-10-13 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_startingbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]