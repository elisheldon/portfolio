# Generated by Django 2.2.5 on 2019-10-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20191008_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliouser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
