# Generated by Django 5.0.4 on 2024-05-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_internet_movil_cargo_fijo_suscr'),
    ]

    operations = [
        migrations.CreateModel(
            name='INTERNET_MOVIL_DEMANDA_INGRESOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANNO', models.IntegerField()),
                ('TRIMESTRE', models.IntegerField()),
                ('MES_DEL_TRIMESTRE', models.IntegerField()),
                ('ID_EMPRESA', models.IntegerField()),
                ('EMPRESA', models.CharField(max_length=100)),
                ('ID_MODALIDAD_PAGO', models.IntegerField()),
                ('MODALIDAD_PAGO', models.CharField(max_length=100)),
                ('ID_TERMINAL', models.IntegerField()),
                ('TERMINAL', models.TextField()),
                ('INGRESOS', models.IntegerField()),
            ],
        ),
    ]