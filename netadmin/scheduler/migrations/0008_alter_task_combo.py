# Generated by Django 4.1.3 on 2022-11-29 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoip', '0002_combo'),
        ('scheduler', '0007_alter_task_combo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='combo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geoip.combo'),
        ),
    ]
