# Generated by Django 4.2 on 2023-04-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Existencia'),
        ),
    ]
