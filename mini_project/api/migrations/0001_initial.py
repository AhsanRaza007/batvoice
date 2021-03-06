# Generated by Django 3.0.6 on 2020-05-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charset', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcription', models.CharField(max_length=500, null=True)),
                ('audio', models.FilePathField(path='./media')),
                ('transcribed', models.BooleanField(default=False)),
                ('user', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
