# Generated by Django 3.0.6 on 2020-05-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbil', '0009_auto_20200511_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatrical',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
