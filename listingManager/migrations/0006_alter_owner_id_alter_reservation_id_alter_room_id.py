# Generated by Django 4.0 on 2021-12-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingManager', '0005_auto_20211227_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
