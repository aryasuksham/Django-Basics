# Generated by Django 4.2.7 on 2023-11-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_alter_subjectmark_student_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
