# Generated by Django 4.2.1 on 2023-11-27 07:48

from django.db import migrations, models
import django.db.models.deletion

#from pharmacy.models import Symptome


def insert_correspondance_default_values(apps, schema_editor):
    # Add the default values for Symptome
    Symptome = apps.get_model('pharmacy', 'Symptome')
    Maladie = apps.get_model('pharmacy', 'Maladie')
    Correspondance = apps.get_model('pharmacy', 'Correspondance')

    # Add all Symptome instances
    symptome_data = [
        'DIARRHEE',
        'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES',
        'NAUSEES et VOMISSEMENTS',
        'FIEVRES LEGERE MAL DE TETE',
        'PERTE D''APPETIT et Fatigue',
        'Douleurs abdominales',
        'Toux',
        'Vomissements',
        'Éruptions cutanées',
        'Une toux persistante (pouvant durer plus de 2 semaines, accompagnée parfois de sang ou de mucosité)',
        'Douleurs thoraciques',
        'Faiblesses ou fatigue',
        'Perte de poids',
        'Perte d’appétit',
        'Des frissons',
        'fièvre',
        'Sueurs nocturnes',
        'Perte de poids involontaire',
        'Fièvre persistante',
        'Fatigue extrême',
        'Infections opportunistes fréquentes',
        'Essoufflement',
        'Toux persistante',
        'Ulcères buccaux',
        'Éruptions cutanées persistantes',
        'Maux de tête persistants',
        'La Cécité',
        'Dermatite Chronique',
        'Atteintes articulaire',
        'lésions cutanéesNodule cutanées',
    ]

    Symptome.objects.bulk_create([Symptome(nom_symptome=symptome_name) for symptome_name in symptome_data])

    # Add the default values for Maladie
    maladie_data = [
        'PALUDISME',
        'VARICELLE',
        'TYPHOIDE',
        'TUBERCULOSE',
        'SIDA',
        'onchocercose',
        'GONORRHEE',
    ]

    Maladie.objects.bulk_create([Maladie(nom_maladie=maladie_name) for maladie_name in maladie_data])

    # Add the default values for Correspondance
    correspondance_data = [
        ('DIARRHEE', 'PALUDISME'),
        ('CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'VARICELLE'),
        ('NAUSEES et VOMISSEMENTS', 'TYPHOIDE'),
        ('FIEVRES LEGERE MAL DE TETE', 'TUBERCULOSE'),
        ('PERTE D''APPETIT et Fatigue', 'SIDA'),
        ('Douleurs abdominales', 'onchocercose'),
        ('Toux', 'GONORRHEE'),
        ('Vomissements', 'PALUDISME'),
        ('Éruptions cutanées', 'VARICELLE'),
        ('Une toux persistante (pouvant durer plus de 2 semaines, accompagnée parfois de sang ou de mucosité)',
         'TYPHOIDE'),
        ('Douleurs thoraciques', 'TUBERCULOSE'),
        ('Faiblesses ou fatigue', 'SIDA'),
        ('Perte de poids', 'onchocercose'),
        ('Perte d’appétit', 'GONORRHEE'),
        ('Des frissons', 'PALUDISME'),
        ('fièvre', 'VARICELLE'),
        ('Sueurs nocturnes', 'TYPHOIDE'),
        ('Perte de poids involontaire', 'TUBERCULOSE'),
        ('Fièvre persistante', 'SIDA'),
        ('Fatigue extrême', 'onchocercose'),
        ('Infections opportunistes fréquentes', 'GONORRHEE'),
        ('Essoufflement', 'PALUDISME'),
        ('Toux persistante', 'VARICELLE'),
        ('Ulcères buccaux', 'TYPHOIDE'),
        ('Éruptions cutanées persistantes', 'TUBERCULOSE'),
        ('Maux de tête persistants', 'SIDA'),
        ('La Cécité', 'onchocercose'),
        ('Dermatite Chronique', 'GONORRHEE'),
        ('Atteintes articulaire', 'PALUDISME'),
        ('lésions cutanéesNodule cutanées', 'VARICELLE'),
    ]

    for symptome_name, maladie_name in correspondance_data:
        symptome = Symptome.objects.get(nom_symptome=symptome_name)
        maladie = Maladie.objects.get(nom_maladie=maladie_name)
        Correspondance.objects.create(symptome=symptome, maladie=maladie)


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_prescription_allergies_and_more'),
    ]

    operations = [
        #migrations.RunPython(insert_correspondance_default_values),
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_maladie', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Symptome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_symptome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maladie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.maladie')),
                ('symptome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.symptome')),
            ],
            options={
                'unique_together': {('maladie', 'symptome')},
            },
        ),
        migrations.RunPython(insert_correspondance_default_values),
    ]