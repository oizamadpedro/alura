# Generated by Django 4.2 on 2023-04-20 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0009_aluno_matriculado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='matriculado',
        ),
    ]
