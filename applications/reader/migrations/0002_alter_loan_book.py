# Generated by Django 4.2 on 2023-04-11 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_category'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_related', to='book.book', verbose_name='Titulo del Libro'),
        ),
    ]
