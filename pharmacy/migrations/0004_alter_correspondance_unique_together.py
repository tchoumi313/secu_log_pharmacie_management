# Generated by Django 4.2.1 on 2023-11-27 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_maladie_symptome_correspondre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='correspondance',
            unique_together={('symptome', 'maladie')},
        ),
    ]
