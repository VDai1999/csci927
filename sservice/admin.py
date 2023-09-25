from django.contrib import admin
from .models import Student, Activity, Student_Activity_Enrollment, No_Show_Records

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)


class ActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Activity, ActivityAdmin)


class StudentActivityEnrollmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student_Activity_Enrollment, StudentActivityEnrollmentAdmin)


class NoShowRecordsAdmin(admin.ModelAdmin):
    pass

admin.site.register(No_Show_Records, NoShowRecordsAdmin)