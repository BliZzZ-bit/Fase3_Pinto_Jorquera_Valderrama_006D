# Generated by Django 3.1.2 on 2020-12-01 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20201130_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='fechingreso',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
