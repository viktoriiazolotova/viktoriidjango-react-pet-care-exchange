# Generated by Django 4.1.5 on 2023-01-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0002_rename_pet_type_petsitter_pet_type_take_care'),
    ]

    operations = [
        migrations.AddField(
            model_name='petsitter',
            name='is_looking_for_help',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='state',
            field=models.CharField(default='', max_length=2),
        ),
    ]