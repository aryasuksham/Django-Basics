# Generated by Django 4.2.7 on 2023-11-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
