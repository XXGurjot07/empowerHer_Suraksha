# Generated by Django 3.0.6 on 2020-05-21 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200521_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
