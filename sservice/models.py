from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_num = models.CharField(max_length=6, unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="password")
    email = models.CharField(max_length=50, unique=True)
    dob = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.id}, {self.student_num}, {self.user_name}, {self.first_name}, {self.last_name}, {self.email}, {self.dob}, {self.phone}"


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    activity_num = models.CharField(max_length=6, unique=True)
    activity_name = models.CharField(max_length=200, default="")
    date_time_to_organize = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.id}, {self.activity_num}, {self.activity_name}, {self.date_time_to_organize}"


class Student_Activity_Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date_time_enrolled = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, default="") # either enroll or disenroll (can force a constraint here - optional)

    def __str__(self):
        return f"{self.id}, {self.student_id}, {self.activity_id}, {self.date_time_enrolled}, {self.status}"


class No_Show_Records(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    no_show_num = models.IntegerField(default=0)
    semester = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.id}, {self.student_id}, {self.no_show_num}, {self.semester}"