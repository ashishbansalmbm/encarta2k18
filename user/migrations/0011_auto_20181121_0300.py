# Generated by Django 2.0 on 2018-11-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_event_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='prize',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
