from django.contrib import admin
# from .models import Student, Activity, Student_Activity_Enrollment, No_Show_Records
from .models import *


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_num', 'user_name', 'first_name', 'last_name', 'email')
    # list_filter = ('user_name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_num', 'activity_name', 'num_of_spots', 'date_time_to_organize')


@admin.register(Student_Activity_Enrollment)
class StudentActivityEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'activity', 'date_time_enrolled', 'status')


@admin.register(No_Show_Records)
class NoShowRecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'activity', 'date_time_records')