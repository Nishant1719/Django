# Generated by Django 5.2.1 on 2025-06-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]
