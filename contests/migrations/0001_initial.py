# Generated by Django 2.2.3 on 2019-09-23 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photologue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='', max_length=4)),
                ('problems', models.CharField(max_length=500)),
                ('final_ranking_onsite', models.CharField(max_length=500)),
                ('final_ranking_online', models.CharField(max_length=500)),
                ('poster', models.ImageField(upload_to='', verbose_name='poster')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photologue.Photo')),
                ('thumbnail_url', models.TextField(verbose_name='thumbnail_url')),
                ('thumbnail_size', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contest_photo', to='photologue.PhotoSize')),
            ],
            options={
                'verbose_name': 'Contest Photo',
            },
            bases=('photologue.photo',),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('gallery_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photologue.Gallery')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='contests.Contest')),
            ],
            options={
                'verbose_name': 'Contest Gallery',
                'verbose_name_plural': 'Contest Galleries',
            },
            bases=('photologue.gallery',),
        ),
        migrations.CreateModel(
            name='CurrentContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.ForeignKey(on_delete=models.SET('get_latest_contest'), to='contests.Contest')),
            ],
            options={
                'verbose_name_plural': 'Current Contest',
            },
        ),
    ]
