# Generated by Django 4.2.15 on 2024-08-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='app_label',
            field=models.CharField(default='pending_game', max_length=80),
        ),
    ]
