# Generated by Django 4.1.3 on 2022-11-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_alter_task_combo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='freq_interval',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='freq_type',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_of_day',
            field=models.TimeField(),
        ),
    ]
