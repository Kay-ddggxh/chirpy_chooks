# Generated by Django 3.2 on 2023-03-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_alter_response_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-create_date'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.AddField(
            model_name='entrytype',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
