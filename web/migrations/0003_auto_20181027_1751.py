# Generated by Django 2.1.2 on 2018-10-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20181027_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='message',
            name='url',
            field=models.CharField(max_length=55),
        ),
    ]