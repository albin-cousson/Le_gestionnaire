# Generated by Django 3.1 on 2020-09-24 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Le_gestionnaire_app', '0013_auto_20200924_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme_model',
            name='main_categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Le_gestionnaire_app.main_idea_model'),
        ),
    ]