# Generated by Django 2.1.3 on 2018-11-26 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('detalle', models.CharField(max_length=300)),
                ('estado', models.CharField(choices=[('Rescatado', 'rescatado'), ('Disponible', 'disponible'), ('Adoptado', 'adoptado')], max_length=20)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
