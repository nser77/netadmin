# Generated by Django 4.1.3 on 2022-11-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoip', '0004_alter_combo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='address_list_prefix',
            field=models.CharField(default='geoip', max_length=33),
        ),
    ]
