# Generated by Django 2.1 on 2018-08-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpcontroller', '0008_auto_20180807_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='muse_device',
            name='name',
            field=models.CharField(blank=True, max_length=24, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rasp_device',
            name='mac_address',
            field=models.CharField(max_length=24, primary_key=True, serialize=False, unique=True),
        ),
    ]
