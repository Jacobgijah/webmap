# Generated by Django 5.0.6 on 2024-06-11 07:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_prohibited_layer_alter_prohibited_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoundaryArea',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'BoundaryArea',
            },
        ),
        migrations.CreateModel(
            name='RiverArea',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'RiverArea',
            },
        ),
        migrations.CreateModel(
            name='WarningArea',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('layer', models.CharField(max_length=254)),
                ('path', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AlterModelOptions(
            name='prohibited',
            options={'verbose_name_plural': 'Prohibited'},
        ),
        migrations.AlterModelOptions(
            name='railway',
            options={'verbose_name_plural': 'Railway'},
        ),
        migrations.AlterModelOptions(
            name='recomended',
            options={'verbose_name_plural': 'Recomended'},
        ),
    ]
