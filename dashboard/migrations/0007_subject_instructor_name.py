# Generated by Django 2.2.19 on 2021-02-23 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210223_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='instructor_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.instructor'),
        ),
    ]