# Generated by Django 2.2.4 on 2019-09-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0011_auto_20190902_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_to_do',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='time_to_do',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
