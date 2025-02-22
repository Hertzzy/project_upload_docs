# Generated by Django 5.0.6 on 2024-05-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_alter_document_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='birthday',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_type',
            field=models.CharField(choices=[('P', 'Prontuário'), ('R', 'Relatório'), ('A', 'Arquivo')], default='P', max_length=1),
        ),
    ]
