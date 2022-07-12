# Generated by Django 4.0.6 on 2022-07-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurVitae', '0005_projects_is_website_projects_tech_used_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='is_source_code',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.CharField(default='default.jpg', max_length=200),
        ),
    ]
