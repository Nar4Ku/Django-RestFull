# Generated by Django 2.2.1 on 2019-05-26 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '0001_initial'),
        ('core', '0003_auto_20190526_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localization.Enderecos'),
            preserve_default=False,
        ),
    ]
