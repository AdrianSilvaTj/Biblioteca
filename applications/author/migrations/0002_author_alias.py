# Generated by Django 4.2 on 2023-04-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='alias',
            field=models.CharField(blank=True, default='alias', max_length=50, verbose_name='Pseudónimo'),
        ),
    ]
