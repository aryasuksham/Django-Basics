# Generated by Django 4.2.7 on 2023-11-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]