# Generated by Django 5.0.4 on 2024-05-08 20:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_usuario_registrado_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Usuario_Registrado',
        ),
    ]