# Generated by Django 2.2.5 on 2019-10-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20191008_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pf_public',
            field=models.BooleanField(default=False),
        ),
    ]
