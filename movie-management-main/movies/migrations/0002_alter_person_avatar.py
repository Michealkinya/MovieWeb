# Generated by Django 4.2.3 on 2023-08-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(upload_to='avatar'),
        ),
    ]