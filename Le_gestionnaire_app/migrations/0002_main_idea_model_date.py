# Generated by Django 3.1 on 2020-09-18 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Le_gestionnaire_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_idea_model',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
