# Generated by Django 2.1 on 2018-10-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0004_auto_20181007_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asientos',
            name='categoria',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='asientos',
            name='numero_asiento',
            field=models.FloatField(max_length=40),
        ),
    ]
