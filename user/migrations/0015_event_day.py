# Generated by Django 2.0 on 2018-11-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20181121_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
