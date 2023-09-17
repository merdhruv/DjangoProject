# Generated by Django 4.2.4 on 2023-09-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciepe_name', models.CharField(max_length=100)),
                ('reciepe_description', models.TextField()),
                ('reciepe_image', models.ImageField(upload_to='reciepe')),
            ],
        ),
    ]
