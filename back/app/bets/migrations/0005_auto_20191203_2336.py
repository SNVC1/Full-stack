# Generated by Django 2.2.7 on 2019-12-03 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0004_auto_20191203_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='bet',
            old_name='player_id',
            new_name='player',
        ),
    ]