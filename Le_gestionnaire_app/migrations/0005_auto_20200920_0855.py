# Generated by Django 3.1 on 2020-09-20 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Le_gestionnaire_app', '0004_auto_20200919_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='second_idea_model',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Le_gestionnaire_app.main_idea_model'),
        ),
    ]