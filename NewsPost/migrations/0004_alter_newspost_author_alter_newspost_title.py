# Generated by Django 4.0.5 on 2022-06-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPost', '0003_alter_newspost_author_alter_newspost_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]