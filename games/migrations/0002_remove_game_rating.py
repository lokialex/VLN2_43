# Generated by Django 3.0.5 on 2020-05-11 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='rating',
        ),
    ]
