# Generated by Django 2.0 on 2018-11-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20181121_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
