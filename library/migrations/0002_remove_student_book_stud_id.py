# Generated by Django 4.2.5 on 2023-11-09 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_book',
            name='stud_id',
        ),
    ]
