# Generated by Django 4.0.6 on 2022-07-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurVitae', '0002_projects_education_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.TextField(default=' - '),
        ),
    ]