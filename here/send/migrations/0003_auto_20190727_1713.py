# Generated by Django 2.1.7 on 2019-07-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0002_auto_20190727_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='mocked',
            field=models.BooleanField(default=True),
        ),
    ]