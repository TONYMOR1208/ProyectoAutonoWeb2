# Generated by Django 5.0.6 on 2024-05-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('año_publicacion', models.IntegerField()),
                ('numero_ejemplares', models.IntegerField()),
            ],
        ),
    ]
