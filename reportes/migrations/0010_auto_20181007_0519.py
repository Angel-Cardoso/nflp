# Generated by Django 2.1 on 2018-10-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0009_auto_20181007_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asientos',
            name='numero_asiento',
            field=models.IntegerField(),
        ),
    ]
