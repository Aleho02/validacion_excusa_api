# Generated by Django 5.2.3 on 2025-06-12 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('excusas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('id_validacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_validacion', models.DateField(auto_now_add=True)),
                ('resultado', models.CharField(choices=[('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')], max_length=10)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('id_excusa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='validacion', to='excusas.excusamedica')),
                ('id_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validaciones', to='usuarios.funcionariovalidador')),
            ],
        ),
    ]
