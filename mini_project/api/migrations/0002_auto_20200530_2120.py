# Generated by Django 3.0.6 on 2020-05-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='transcription',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='transcript',
            name='user',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]
