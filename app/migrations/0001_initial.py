# Generated by Django 4.1.6 on 2023-02-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=256, verbose_name='Institución')),
                ('preescolar', models.BooleanField(default=False, verbose_name='Preescolar')),
                ('primaria', models.BooleanField(default=False, verbose_name='Primaria')),
                ('secundaria', models.BooleanField(default=False, verbose_name='secundaria')),
                ('media', models.BooleanField(default=False, verbose_name='Media')),
                ('meida_tecnica', models.BooleanField(default=False, verbose_name='Media técnica')),
                ('Inscription_DANE', models.PositiveBigIntegerField()),
                ('codigo_ICFES', models.PositiveBigIntegerField()),
                ('sedeA', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Sede A')),
                ('sedeB', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Sede B')),
                ('telefono1', models.PositiveBigIntegerField(blank=True, null=True, unique=True)),
                ('telefono2', models.PositiveBigIntegerField(blank=True, null=True, unique=True)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('web', models.URLField(max_length=256, verbose_name='página web')),
            ],
            options={
                'verbose_name': 'Institucion',
                'verbose_name_plural': 'Instituciones',
                'db_table': 'institucion',
                'ordering': ['name'],
            },
        ),
    ]
