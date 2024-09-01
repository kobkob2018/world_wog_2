# Generated by Django 4.2.15 on 2024-08-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0004_game_css_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
