# Generated by Django 2.1.7 on 2019-07-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0005_auto_20190727_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='jid',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
