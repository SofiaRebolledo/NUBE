# Generated by Django 5.0.4 on 2024-05-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_alter_internet_movil_demanda_ingresos_id_modalidad_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internet_movil_demanda_abonados',
            name='ID_MODALIDAD_PAGO',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='internet_movil_demanda_trafico',
            name='ID_MODALIDAD_PAGO',
            field=models.TextField(),
        ),
    ]
