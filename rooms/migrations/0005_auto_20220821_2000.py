# Generated by Django 2.2.5 on 2022-08-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20220820_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bedromms',
            new_name='bedrooms',
        ),
    ]
