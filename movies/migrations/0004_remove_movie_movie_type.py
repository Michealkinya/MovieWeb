# Generated by Django 4.2.3 on 2023-08-02 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movietype_alter_movie_movie_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_type',
        ),
    ]