# Generated by Django 4.1.3 on 2022-12-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_students_file_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='file_field',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='students',
            name='visa_photo',
            field=models.URLField(blank=True, default='https://cdn5.vectorstock.com/i/1000x1000/54/34/a-student-boy-cartoon-character-isolated-on-white-vector-36115434.jpg', null=True, verbose_name='Снимка за ВИЗА'),
        ),
    ]
