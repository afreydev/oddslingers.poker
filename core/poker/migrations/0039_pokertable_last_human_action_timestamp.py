# Generated by Django 2.0.8 on 2018-12-11 21:52

from django.db import migrations, models


def update_last_human_action_timestamp(apps, schema_editor):
    PokerTable = apps.get_model('poker', 'PokerTable')
    for table in PokerTable.objects.all():
        hand_history = table.handhistory_set.first()
        if hand_history:
            action_set = hand_history.handhistoryaction_set.order_by(
                '-timestamp'
            )
            if action_set:
                last_action = action_set.first()
                table.last_human_action_timestamp = last_action.timestamp
                table.save()


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0038_player_last_action_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokertable',
            name='last_human_action_timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.RunPython(update_last_human_action_timestamp)
    ]
