# Generated by Django 2.2 on 2019-05-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0007_auto_20190523_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entranceexitmodel',
            name='resource',
            field=models.ManyToManyField(blank=True, default=None, related_name='entrance_exit_resource', to='ems_app.ResourceModel', verbose_name='Zasób'),
        ),
    ]
