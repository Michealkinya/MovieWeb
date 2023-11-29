# Generated by Django 4.2.3 on 2023-08-02 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_person_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.movietype'),
        ),
    ]