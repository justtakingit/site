# Generated by Django 2.1.2 on 2018-10-27 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='titile',
            new_name='title',
        ),
    ]
