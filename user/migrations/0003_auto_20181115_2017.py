# Generated by Django 2.0 on 2018-11-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181115_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='current_college',
            new_name='college',
        ),
    ]
