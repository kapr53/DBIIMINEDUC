# Generated by Django 2.2 on 2020-05-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0003_auto_20200519_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante',
            name='padre',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='padre.PadreFamilia', verbose_name='Padre de Familia'),
        ),
    ]
