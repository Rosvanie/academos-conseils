# Generated by Django 5.1.1 on 2024-10-31 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apphome', '0020_remove_programme_moyens_peda_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MoyenPeda',
        ),
        migrations.DeleteModel(
            name='Prerequis',
        ),
        migrations.DeleteModel(
            name='PublicCible',
        ),
    ]
