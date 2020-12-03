# Generated by Django 3.1.2 on 2020-11-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fechamuerte',
            field=models.DateField(blank=True, null=True, verbose_name='Muerto'),
        ),
        migrations.AddField(
            model_name='autor',
            name='fechanac',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]