# Generated by Django 5.0.2 on 2024-11-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('room_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tot_student', models.CharField(max_length=5)),
            ],
        ),
    ]
