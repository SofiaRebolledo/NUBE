# Generated by Django 5.0.4 on 2024-05-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_rename_usuario_usuario_registrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.IntegerField()),
            ],
        ),
    ]