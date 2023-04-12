# Generated by Django 4.2 on 2023-04-12 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('date', models.DateField(verbose_name='Fecha de Lanzamiento')),
                ('image', models.ImageField(blank=True, null=True, upload_to='book')),
                ('visits', models.PositiveIntegerField(verbose_name='Visitas')),
                ('authors', models.ManyToManyField(to='author.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_related', to='book.category')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['title', 'date'],
            },
        ),
    ]
