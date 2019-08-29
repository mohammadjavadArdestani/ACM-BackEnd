# Generated by Django 2.2.3 on 2019-08-28 16:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_level', models.CharField(choices=[('bsc', 'BSc'), ('msc', 'MSc'), ('phd', 'PhD')], max_length=3)),
                ('email', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Phone number must be entered correctly.', regex='09[0-9]{9}')])),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('flag', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_onsite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OnsiteContestant',
            fields=[
                ('contestant_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usermanagement.Contestant')),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large'), ('2XL', '2X-Large'), ('3XL', '3X-Large')], max_length=20)),
            ],
            bases=('usermanagement.contestant',),
        ),
        migrations.AddField(
            model_name='contestant',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermanagement.Team'),
        ),
        migrations.CreateModel(
            name='OnlineContestant',
            fields=[
                ('contestant_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usermanagement.Contestant')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermanagement.Country')),
            ],
            bases=('usermanagement.contestant',),
        ),
    ]