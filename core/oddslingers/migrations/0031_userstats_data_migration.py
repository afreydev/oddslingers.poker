# Generated by Django 2.0.8 on 2018-10-11 16:05
from django.db import migrations
from django.db.models import Sum


def create_userstats(apps, schema_editor):
    """Method to create UserStats for existing users"""
    User = apps.get_model('oddslingers', 'User')
    UserStats = apps.get_model('oddslingers', 'UserStats')
    for user in User.objects.all():
        hands_played = user.player_set.aggregate(
            hands=Sum('n_hands_played')
        )['hands'] or 0
        UserStats.objects.get_or_create(
            user=user,
            hands_played=hands_played
        )


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0030_auto_20181010_1728'),
    ]

    operations = [
        migrations.RunPython(create_userstats)
    ]
