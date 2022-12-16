# Generated by Django 4.1.1 on 2022-12-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seminario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('fechaIns', models.DateField()),
                ('horaIns', models.CharField(max_length=20)),
                ('institucion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=50)),
            ],
        ),
    ]