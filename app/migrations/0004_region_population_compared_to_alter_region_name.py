# Generated by Django 5.0.3 on 2024-05-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_region_area_info_region_image_region_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='population_compared_to',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nomi'),
        ),
    ]
