# Generated by Django 5.0.6 on 2024-05-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('register', models.CharField(max_length=50)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=50)),
                ('doc_tyoe', models.BooleanField()),
                ('birthday', models.CharField(max_length=50)),
            ],
        ),
    ]
