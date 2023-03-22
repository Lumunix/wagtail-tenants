# Generated by Django 3.2.18 on 2023-03-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0003_alter_clientbackup_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientFeature",
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
                ("name", models.CharField(max_length=100)),
                ("menu_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="client",
            name="features",
            field=models.ManyToManyField(blank=True, to="customers.ClientFeature"),
        ),
    ]