# Generated by Django 4.2 on 2023-04-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0014_remove_aluno_exibe_curso_exibe'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='exibe',
            field=models.IntegerField(null=True),
        ),
    ]
