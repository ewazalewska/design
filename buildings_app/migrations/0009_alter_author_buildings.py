# Generated by Django 4.1.6 on 2023-02-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings_app', '0008_author_remove_project_description_project_ceiling_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='buildings',
            field=models.ManyToManyField(related_name='engineers', to='buildings_app.project'),
        ),
    ]
