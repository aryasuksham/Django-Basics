# Generated by Django 4.2.7 on 2023-11-16 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0011_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_report_card_generation')},
        ),
    ]