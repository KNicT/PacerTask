# Generated by Django 4.2.1 on 2023-06-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='is_adult',
            field=models.BooleanField(default=True),
        ),
    ]
