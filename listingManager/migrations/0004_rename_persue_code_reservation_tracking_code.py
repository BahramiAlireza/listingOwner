# Generated by Django 4.0 on 2021-12-27 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listingManager', '0003_alter_owner_id_alter_reservation_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='persue_code',
            new_name='tracking_code',
        ),
    ]
