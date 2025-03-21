# Generated by Django 5.1.6 on 2025-03-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rules", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="occurrence",
            name="outcome",
            field=models.CharField(
                choices=[("BONUS", "Bonus"), ("PENALTY", "Penalty")],
                default="BONUS",
                max_length=10,
            ),
        ),
    ]
