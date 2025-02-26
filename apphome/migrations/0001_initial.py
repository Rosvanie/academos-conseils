# Generated by Django 5.1.1 on 2024-10-25 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thematique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('duree', models.PositiveIntegerField(help_text='Durée de la formation')),
                ('unite_duree', models.CharField(choices=[('heures', 'Heures'), ('jours', 'Jours'), ('semaines', 'Semaines'), ('mois', 'Mois')], default='heures', max_length=10)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('thematique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formations', to='apphome.thematique')),
            ],
        ),
        migrations.AddField(
            model_name='thematique',
            name='type_formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thematiques', to='apphome.typeformation'),
        ),
    ]
