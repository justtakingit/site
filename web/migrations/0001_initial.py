# Generated by Django 2.1.2 on 2018-10-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('titile', models.CharField(max_length=15)),
                ('url', models.CharField(max_length=15)),
            ],
        ),
    ]