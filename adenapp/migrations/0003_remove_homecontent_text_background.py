# Generated by Django 3.2 on 2022-12-01 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adenapp', '0002_auto_20221130_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecontent',
            name='text_background',
        ),
    ]