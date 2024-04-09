# Generated by Django 4.1.13 on 2024-04-03 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zap_scan', '0010_alert_alertinstance_program_site_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertinstance',
            name='alert',
        ),
        migrations.RemoveField(
            model_name='site',
            name='program',
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.DeleteModel(
            name='AlertInstance',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]