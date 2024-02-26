# Generated by Django 5.0.2 on 2024-02-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_person_remove_gun_ammo_c_gun_calibre_gun_count_ammo_and_more')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('classp', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='gun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('calibre', models.CharField(default=1, max_length=50)),
                ('count_ammo', models.IntegerField(default=1)),
                ('serial_number', models.CharField(default=1, max_length=50)),
            ],
        ),
    ]
