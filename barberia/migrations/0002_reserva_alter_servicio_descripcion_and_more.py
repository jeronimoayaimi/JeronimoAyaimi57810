# Generated by Django 5.0.6 on 2024-07-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barberia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=100)),
                ('emailCliente', models.EmailField(max_length=254)),
                ('fechaTurno', models.DateField()),
                ('horaTurno', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.CharField(max_length=60),
        ),
    ]