# Generated by Django 5.1.1 on 2024-10-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphome', '0006_newslettersubscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscriber',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
