# Generated by Django 3.2.5 on 2021-09-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
