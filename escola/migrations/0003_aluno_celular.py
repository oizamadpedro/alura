# Generated by Django 4.2 on 2023-04-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default=False, max_length=14),
        ),
    ]