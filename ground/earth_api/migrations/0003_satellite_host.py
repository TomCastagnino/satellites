# Generated by Django 4.0a1 on 2021-09-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth_api', '0002_auto_20210923_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='host',
            field=models.CharField(default='127.0.0.1', max_length=20),
        ),
    ]