# Generated by Django 3.1.2 on 2021-01-12 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='endusers',
        ),
    ]
