# Generated by Django 2.0.4 on 2019-07-09 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoringTool', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeesprofile',
            old_name='employee_Address',
            new_name='employee_address',
        ),
    ]