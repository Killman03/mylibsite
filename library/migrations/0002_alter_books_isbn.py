# Generated by Django 4.2.4 on 2023-12-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="ISBN",
            field=models.CharField(blank=True, null=True),
        ),
    ]
