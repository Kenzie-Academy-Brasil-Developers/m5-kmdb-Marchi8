# Generated by Django 4.1 on 2022-12-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="budget",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
