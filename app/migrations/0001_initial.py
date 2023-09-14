# Generated by Django 4.1.4 on 2023-01-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256)),
                ('user_level', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('zf', models.IntegerField()),
                ('pl', models.IntegerField()),
                ('dz', models.IntegerField()),
                ('start_time', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=128)),
                ('topic_name', models.CharField(max_length=128)),
                ('discuss_number', models.CharField(max_length=64)),
                ('read_number', models.CharField(max_length=64)),
            ],
        ),
    ]
