# Generated by Django 5.0.4 on 2024-05-08 20:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_usuario_registrado_delete_analista_delete_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario_registrado',
            new_name='Usuario',
        ),
    ]
