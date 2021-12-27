# Generated by Django 3.1 on 2021-12-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingManager', '0004_rename_persue_code_reservation_tracking_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='reservations',
        ),
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]