# Generated by Django 3.2.13 on 2022-07-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='url',
            field=models.URLField(default='https://bitcoinerjobs.com/', max_length=300),
            preserve_default=False,
        ),
    ]
