# Generated by Django 3.1.1 on 2020-12-01 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201201_0510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='disabled',
            new_name='is_disabled',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='news',
            new_name='is_news',
        ),
    ]