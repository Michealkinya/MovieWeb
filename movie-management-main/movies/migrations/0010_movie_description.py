# Generated by Django 4.2.3 on 2023-08-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_person_about_person_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
            preserve_default=False,
        ),
    ]
