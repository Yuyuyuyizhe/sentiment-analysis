# Generated by Django 4.1.4 on 2023-01-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_wordcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=24)),
            ],
        ),
    ]
