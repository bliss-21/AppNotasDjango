# Generated by Django 4.0.4 on 2022-05-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='deleted_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]