# Generated by Django 5.0.6 on 2024-06-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_prohibited_pid_alter_prohibited_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prohibited',
            name='pid',
        ),
    ]
