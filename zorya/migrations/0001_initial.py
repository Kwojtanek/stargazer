# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import zorya.fields
import zorya.thumbs


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AstroCharts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=16)),
                ('maxAscension', models.TimeField()),
                ('minAscension', models.TimeField()),
                ('maxDeclination', zorya.fields.DeclinationField(null=True, blank=True)),
                ('minDeclination', zorya.fields.DeclinationField(null=True, blank=True)),
                ('magnitudo', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('description', models.CharField(max_length=1024, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constellations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbreviation', models.CharField(unique=True, max_length=3)),
                ('constellation', models.CharField(unique=True, max_length=128)),
                ('other_abbreviation', models.CharField(unique=True, max_length=4)),
                ('genitive', models.CharField(unique=True, max_length=128)),
                ('family', models.CharField(max_length=32)),
                ('origin', models.CharField(max_length=64)),
                ('meaning', models.CharField(max_length=128)),
                ('brightest_star', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectPhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('photo', zorya.thumbs.ImageWithThumbsField(null=True, upload_to=b'images', blank=True)),
                ('photo_url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objects_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_number', models.CharField(max_length=16)),
                ('object_catalogue', models.ForeignKey(related_name='Catalogue', to='zorya.Catalogues')),
            ],
        ),
        migrations.CreateModel(
            name='StellarObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_name', models.CharField(unique=True, max_length=32)),
                ('type', models.CharField(max_length=100, null=True, blank=True)),
                ('type_shortcut', models.CharField(max_length=12, null=True, blank=True)),
                ('classe', models.CharField(max_length=12, null=True, blank=True)),
                ('rightAsc', models.TimeField(null=True, blank=True)),
                ('declination', zorya.fields.DeclinationField(null=True, blank=True)),
                ('distance', models.IntegerField(null=True, blank=True)),
                ('magnitudo', models.FloatField(max_length=5, null=True, blank=True)),
                ('dimAxb', models.CharField(max_length=32, null=True, blank=True)),
                ('pa', models.SmallIntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=128, null=True, blank=True)),
                ('id1', models.CharField(max_length=32, null=True, blank=True)),
                ('id2', models.CharField(max_length=32, null=True, blank=True)),
                ('id3', models.CharField(max_length=32, null=True, blank=True)),
                ('notes', models.CharField(max_length=64, null=True, blank=True)),
                ('overview', models.TextField(null=True, blank=True)),
                ('constelation', models.ForeignKey(related_name='ngcs', to='zorya.Constellations')),
            ],
        ),
        migrations.CreateModel(
            name='testur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='objects_list',
            name='single_object',
            field=models.ForeignKey(related_name='catalogues', to='zorya.StellarObject'),
        ),
        migrations.AddField(
            model_name='objectphotos',
            name='ngc_object',
            field=models.ForeignKey(related_name='photos', to='zorya.StellarObject'),
        ),
    ]
