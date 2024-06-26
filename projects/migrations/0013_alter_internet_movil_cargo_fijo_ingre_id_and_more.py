# Generated by Django 5.0.4 on 2024-05-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_internet_movil_demanda_ingresos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internet_movil_cargo_fijo_ingre',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internet_movil_cargo_fijo_suscr',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internet_movil_cargo_fijo_trafi',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internet_movil_demanda_abonados',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internet_movil_demanda_ingresos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internet_movil_demanda_trafico',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
