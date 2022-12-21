# Generated by Django 4.1.3 on 2022-11-29 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoip', '0002_combo'),
        ('scheduler', '0010_alter_task_combo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='combo',
            field=models.OneToOneField(help_text='Select a Combo', on_delete=django.db.models.deletion.CASCADE, to='geoip.combo'),
        ),
    ]
