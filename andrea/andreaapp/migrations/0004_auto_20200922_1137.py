# Generated by Django 2.2.12 on 2020-09-22 11:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('andreaapp', '0003_categorie_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='content',
        ),
        migrations.AddField(
            model_name='fashion',
            name='content',
            field=tinymce.models.HTMLField(null=True, verbose_name='content'),
        ),
    ]
