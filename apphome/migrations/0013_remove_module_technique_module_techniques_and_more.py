# Generated by Django 5.1.1 on 2024-10-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphome', '0012_technique_module_nom_module_technique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='technique',
        ),
        migrations.AddField(
            model_name='module',
            name='techniques',
            field=models.ManyToManyField(blank=True, related_name='modules', to='apphome.technique'),
        ),
        migrations.AlterField(
            model_name='module',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='titre',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.RemoveField(
            model_name='programme',
            name='modules',
        ),
        migrations.AddField(
            model_name='programme',
            name='modules',
            field=models.ManyToManyField(blank=True, related_name='programmes', to='apphome.module'),
        ),
    ]
