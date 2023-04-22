# Generated by Django 4.1.7 on 2023-04-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="signup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email_address", models.CharField(max_length=50)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=25)),
                ("confirm_password", models.CharField(max_length=25)),
                ("country", models.CharField(max_length=25)),
                ("address", models.CharField(max_length=25)),
            ],
        ),
    ]
