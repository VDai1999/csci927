# Generated by Django 3.1.1 on 2023-09-14 10:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_num', models.CharField(max_length=6, unique=True)),
                ('activity_name', models.CharField(default='', max_length=200)),
                ('date_time_to_organize', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_num', models.CharField(max_length=6, unique=True)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='password', max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Activity_Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time_enrolled', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='', max_length=10)),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sservice.activity')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sservice.student')),
            ],
        ),
    ]
