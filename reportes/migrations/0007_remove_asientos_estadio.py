# Generated by Django 2.1 on 2018-10-07 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0006_auto_20181007_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asientos',
            name='estadio',
        ),
    ]