# Generated by Django 2.2.7 on 2019-12-14 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0017_auto_20191214_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 14, 15, 47, 8, 269011, tzinfo=utc)),
        ),
    ]