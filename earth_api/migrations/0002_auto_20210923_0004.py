# Generated by Django 3.2.7 on 2021-09-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='port',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]