# Generated by Django 2.2.4 on 2019-08-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_todolist_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
