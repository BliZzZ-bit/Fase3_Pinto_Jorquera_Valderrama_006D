# Generated by Django 3.1.2 on 2020-11-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20201106_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='fechamuerte',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de defuncion'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='fechanac',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='papellido',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='pnombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]
