# Generated by Django 5.1.7 on 2025-03-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='ToDoList',
            new_name='todolist',
        ),
        migrations.AddField(
            model_name='item',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
