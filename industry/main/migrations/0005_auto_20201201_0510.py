# Generated by Django 3.1.1 on 2020-12-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200930_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='news',
            field=models.BooleanField(default=False),
        ),
    ]
