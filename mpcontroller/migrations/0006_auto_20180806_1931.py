# Generated by Django 2.1 on 2018-08-06 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpcontroller', '0005_muse_device_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rasp_device',
            old_name='ip_address',
            new_name='mac_address',
        ),
    ]
