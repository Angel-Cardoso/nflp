# Generated by Django 2.1 on 2018-10-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0011_auto_20181007_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='palcos',
            name='estado',
            field=models.CharField(default='disponible', max_length=5),
        ),
    ]
