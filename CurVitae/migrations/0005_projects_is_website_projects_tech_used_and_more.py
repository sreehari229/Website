# Generated by Django 4.0.6 on 2022-07-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurVitae', '0004_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='is_website',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projects',
            name='tech_used',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='projects',
            name='website_link',
            field=models.TextField(default=' '),
        ),
    ]
