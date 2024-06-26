# Generated by Django 5.0.3 on 2024-04-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceid', models.CharField(max_length=10)),
                ('other', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=10)),
                ('evidence', models.TextField()),
                ('pluginId', models.CharField(max_length=10)),
                ('cweid', models.CharField(max_length=10)),
                ('confidence', models.CharField(max_length=10)),
                ('wascid', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('messageId', models.CharField(max_length=10)),
                ('inputVector', models.TextField()),
                ('url', models.URLField()),
                ('reference', models.URLField()),
                ('solution', models.TextField()),
                ('alert', models.CharField(max_length=255)),
                ('param', models.CharField(max_length=255)),
                ('attack', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('risk', models.CharField(max_length=10)),
                ('alertRef', models.CharField(max_length=20)),
            ],
        ),
    ]
