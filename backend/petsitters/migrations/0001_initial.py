# Generated by Django 4.1.5 on 2023-01-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petsitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('zipcode', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('is_available_help', models.BooleanField(default=False)),
                ('pet_type', models.CharField(max_length=50)),
            ],
        ),
    ]