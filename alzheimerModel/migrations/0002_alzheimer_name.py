# Generated by Django 4.2.7 on 2023-12-19 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alzheimerModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alzheimer',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
