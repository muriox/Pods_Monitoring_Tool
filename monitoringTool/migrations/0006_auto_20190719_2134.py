# Generated by Django 2.0.4 on 2019-07-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoringTool', '0005_auto_20190719_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicesconfiguration',
            name='device_config_id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
