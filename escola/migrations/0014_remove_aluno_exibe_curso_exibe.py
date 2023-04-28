# Generated by Django 4.2 on 2023-04-25 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0013_aluno_exibe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='exibe',
        ),
        migrations.AddField(
            model_name='curso',
            name='exibe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.aluno'),
        ),
    ]
