# Generated by Django 3.0.6 on 2020-05-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbil', '0007_auto_20200511_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='address',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='theater',
            name='description',
            field=models.TextField(default=' ', max_length=1023),
        ),
        migrations.AlterField(
            model_name='theater',
            name='email',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='theater',
            name='phone',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='theater',
            name='schedule',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
