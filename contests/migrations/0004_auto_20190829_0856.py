# Generated by Django 2.2.4 on 2019-08-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20190828_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acm',
            name='problems',
            field=models.CharField(max_length=500),
        ),
    ]
