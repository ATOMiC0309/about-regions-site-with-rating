# Generated by Django 5.0.3 on 2024-05-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_region_population_compared_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]
