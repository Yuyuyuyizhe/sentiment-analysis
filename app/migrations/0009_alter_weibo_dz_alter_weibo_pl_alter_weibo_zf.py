# Generated by Django 4.1.4 on 2023-01-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_analyseresult_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weibo',
            name='dz',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='pl',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='zf',
            field=models.CharField(max_length=16),
        ),
    ]
