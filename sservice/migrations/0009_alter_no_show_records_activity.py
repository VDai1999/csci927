# Generated by Django 4.2.6 on 2023-10-16 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sservice", "0008_no_show_records_date_time_records"),
    ]

    operations = [
        migrations.AlterField(
            model_name="no_show_records",
            name="activity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="sservice.activity",
            ),
        ),
    ]