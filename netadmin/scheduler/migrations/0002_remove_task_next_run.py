# Generated by Django 4.1.3 on 2022-11-28 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='next_run',
        ),
    ]
