# Generated by Django 2.2.12 on 2020-09-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='marp_url',
        ),
        migrations.AddField(
            model_name='infocontact',
            name='marp_url',
            field=models.TextField(null=True),
        ),
    ]
