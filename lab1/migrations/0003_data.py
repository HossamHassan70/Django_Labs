# Generated by Django 3.2.12 on 2024-02-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0002_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('track', models.EmailField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
            ],
        ),
    ]
