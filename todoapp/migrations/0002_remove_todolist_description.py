# Generated by Django 2.2.4 on 2019-08-20 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='description',
        ),
    ]
