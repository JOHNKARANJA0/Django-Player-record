# Generated by Django 4.2.17 on 2024-12-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PLAYER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=10)),
                ('pname', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('game', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'player',
            },
        ),
    ]
