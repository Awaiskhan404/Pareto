# Generated by Django 2.2.19 on 2021-02-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_subject_subject_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='Course_name',
            field=models.CharField(choices=[('ENGLISH', 'ENGLISH'), ('MATH', 'MATH'), ('PYTHON', 'PYTHON')], default='SELECT COURSE', max_length=50),
        ),
    ]
