# Generated by Django 3.2.11 on 2022-01-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercial',
            name='experience',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
