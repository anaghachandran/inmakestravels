# Generated by Django 4.2.4 on 2023-09-04 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='dis',
            new_name='desc',
        ),
    ]