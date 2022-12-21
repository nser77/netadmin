# Generated by Django 4.1.3 on 2022-12-01 22:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('geoip', '0006_alter_combo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
