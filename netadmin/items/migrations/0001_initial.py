# Generated by Django 4.1.3 on 2022-11-28 00:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('consumer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.consumer')),
            ],
        ),
    ]
