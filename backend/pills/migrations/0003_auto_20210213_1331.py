# Generated by Django 3.1.6 on 2021-02-13 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0002_plans_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pills',
            name='schedule',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('pill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pills.pills')),
            ],
        ),
    ]
