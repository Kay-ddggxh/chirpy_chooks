# Generated by Django 3.2 on 2023-02-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]