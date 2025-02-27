# Generated by Django 5.1.3 on 2024-11-06 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('genre', models.CharField(max_length=100, verbose_name='Genre')),
                ('publication_year', models.PositiveIntegerField(verbose_name='Publication Year')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['-publication_year'],
            },
        ),
    ]
