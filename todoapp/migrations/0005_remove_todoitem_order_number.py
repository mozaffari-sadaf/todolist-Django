# Generated by Django 2.2.4 on 2019-08-21 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20190821_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='order_number',
        ),
    ]
