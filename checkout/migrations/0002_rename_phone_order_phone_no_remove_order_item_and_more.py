# Generated by Django 4.2.5 on 2023-11-03 10:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='phone_no',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=None, null=True, size=None),
        ),
    ]