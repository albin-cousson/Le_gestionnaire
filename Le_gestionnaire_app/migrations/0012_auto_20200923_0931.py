# Generated by Django 3.1 on 2020-09-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Le_gestionnaire_app', '0011_auto_20200922_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_idea_model',
            name='idea',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='programme_model',
            name='idea',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='second_idea_model',
            name='idea',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='third_idea_model',
            name='idea',
            field=models.CharField(max_length=100),
        ),
    ]