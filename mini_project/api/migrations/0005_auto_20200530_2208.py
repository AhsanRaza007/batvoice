# Generated by Django 3.0.6 on 2020-05-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200530_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='transcription',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='transcript',
            name='user',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
