# Generated by Django 3.2.7 on 2021-09-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.CharField(max_length=100),
        ),
    ]
