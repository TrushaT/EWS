# Generated by Django 3.1.6 on 2021-02-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='destination',
            field=models.CharField(default='', max_length=100),
        ),
    ]