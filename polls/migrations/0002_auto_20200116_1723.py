# Generated by Django 3.0.2 on 2020-01-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]
