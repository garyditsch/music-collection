# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('artists', models.ManyToManyField(to='artists.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('album', models.ManyToManyField(to='tracks.Album')),
                ('artists', models.ManyToManyField(to='artists.Artist')),
                ('genres', models.ManyToManyField(to='tracks.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(to='tracks.Genre'),
        ),
    ]
