# Generated by Django 3.1.1 on 2023-10-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sservice', '0004_auto_20231005_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_activity_enrollment',
            name='date_time_enrolled',
            field=models.DateField(auto_now_add=True),
        ),
    ]
