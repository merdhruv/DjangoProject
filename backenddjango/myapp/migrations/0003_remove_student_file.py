# Generated by Django 4.2.4 on 2023-09-13 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='File',
        ),
    ]