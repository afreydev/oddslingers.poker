# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0003_auto_20170923_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='name',
            field=models.CharField(choices=[('hello_world', 'filled out profile information'), ('shove', 'bet or raise all-in'), ('big_bluff', 'win a 200bb+ pot without showdown with a bottom 20%% hand, and show it'), ('big_call', 'call a 50bb+ bet on the river with a bottom 20%% hand, and win'), ('big_win', 'win a 500bb+ pot'), ('run_bad', 'lose 500bbs or more in a continuous session'), ('marathon', 'play 1,000 hands in a continuous session'), ('adept', 'play at least 50,000 total hands'), ('the_duck', 'win a 400bb+ pot with 72o at showdown'), ('quads', 'win with four-of-a-kind'), ('straight_flush', 'win with a straight flush at showdown'), ('steel_wheel', 'win with an ace-to-5 straight flush at showdown'), ('royalty', 'win with a royal flush at showdown'), ('the_teddy', 'win with pocket aces against an Ax full house'), ('mike_mcd', 'lose with an Ax full house against pocket aces '), ('its_a_trap', 'check-raise all-in on the river, get called, and win'), ('cool_hand_luke', 'win a 500bb+ pot with a bottom 5%% hand'), ('bombs_away', 'win a 300bb+ pot without ever facing a bet or raise'), ('true_grit', 'win a 500bb+ pot without ever betting or raising'), ('double_check_raise', 'check-raise twice in the same hand and win the pot'), ('trifecta', 'check-raise, check-raise, check-raise all-in and win'), ('quadfecta', 'limp- or call-reraise, plus a trifecta'), ('soul_reader', 'call on the river and win a pot with Jx or worse and no pair'), ('tourney_winner', 'win a multi-table tournament'), ('champion', 'win a tournament with at least 500 entrants'), ('because_it_is_there', 'be the king-of-the-hill at the end of a week'), ('so_many_chips', 'obtain a play-chip balance of 1,000,000 chips or more'), ('play_chip_diety', 'obtain a play-chip balance of 9,999,999 chips or more'), ('nice_session', 'win 500bbs or more in a continuous session'), ('heater', 'win at least 1000 bbs in one session'), ('sizzler', 'win 1500 bbs in a 24-hour period'), ('god_mode', 'win at least 2000 bbs in one session'), ('bad_beat', 'lose with aces-full (using both holecards) or better'), ('cooler', 'lose 300bbs or more with top 0.1%% hand'), ('suckout', 'win an all-in with 1%% equity'), ('hes_on_fire', 'get all-in and win three times in a row'), ('this_is_rigged', 'lose 1000bbs or more in a continuous session'), ('just_one_more_hand', 'play 5,000 hands in a continuous session'), ('cant_stop_wont_stop', 'play 10,000 hands in a continuous session and in at least 500bbs'), ('grinder', 'play 50,000 hands in a month'), ('true_grinder', 'play 100,000 hands in a month'), ('capital_g_grinder', 'play the more hands than any other player in a month'), ('fiend', 'play 500,000 hands in a 1-year period'), ('veteran', 'play at least 100,000 total hands'), ('pro', 'play at least 500,000 total hands'), ('seen_it_all', 'play a total of 1,000,000 hands'), ('bug_hunter', 'report a bug that gets fixed'), ('genesis', 'one of the first 1000 accounts'), ('early_bird', 'open an account before 2019'), ('badgiest_badger', 'the player with the most badges'), ('king_of_the_hill', 'the biggest winner this week so far in KOTH points'), ('good_samaritan', 'manually awarded for recognized good behaviour'), ('streamer', 'stream a session'), ('popular_streamer', 'streamed play and got 100+ simultaneous viewers'), ('do_unto_others', 'positive "handshake" balance'), ('black_hat', 'attempt a technical exploit against Blitzka'), ('potty_mouth', 'attempted to use swear words in username or profile bio')], max_length=32),
        ),
    ]
