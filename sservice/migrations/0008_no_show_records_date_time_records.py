# Generated by Django 4.2.5 on 2023-10-08 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("sservice", "0007_no_show_records"),
    ]

    operations = [
        migrations.AddField(
            model_name="no_show_records",
            name="date_time_records",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
