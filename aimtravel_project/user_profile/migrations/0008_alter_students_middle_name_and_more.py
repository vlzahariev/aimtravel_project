# Generated by Django 4.1.3 on 2022-12-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_students_bg_personal_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='middle_name',
            field=models.CharField(blank=True, default='-', max_length=15, null=True, verbose_name='Презиме'),
        ),
        migrations.AlterField(
            model_name='students',
            name='passport_date_of_issue',
            field=models.DateField(blank=True, null=True, verbose_name='Дата на издаване'),
        ),
    ]
