# Generated by Django 2.2 on 2019-07-11 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources_app', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntranceExitReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_description', models.CharField(max_length=200, verbose_name='opis')),
            ],
        ),
        migrations.CreateModel(
            name='EntranceExitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Data rozpoczęcia')),
                ('end_date', models.DateField(verbose_name='Data zakończenia')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Czy zatwierdzone')),
                ('place', models.CharField(max_length=200, verbose_name='Miejsce')),
                ('fromExitToEntranceTimestamp', models.IntegerField(blank=True, default=None, null=True, verbose_name='Czas')),
                ('approver_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrance_exit_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Osoba zatwierdzająca')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrance_exit_project', to='project_app.ProjectModel', verbose_name='Projekt')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrance_exit_reason', to='entrance_exit_app.EntranceExitReason', verbose_name='Powód')),
                ('resource', models.ManyToManyField(blank=True, default=None, related_name='entrance_exit_resource', to='resources_app.ResourceModel', verbose_name='Zasób')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrance_exit_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik')),
            ],
        ),
    ]
