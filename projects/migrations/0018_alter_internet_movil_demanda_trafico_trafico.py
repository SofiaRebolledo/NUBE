# Generated by Django 5.0.4 on 2024-05-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_alter_internet_movil_demanda_abonados_id_modalidad_pago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internet_movil_demanda_trafico',
            name='TRAFICO',
            field=models.BigIntegerField(),
        ),
    ]
