from django.db import models
from django.db.models import Count, F, Q
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

from datetime import datetime, timedelta


class Activity_View(APIView):
    def get(self, request):
        """
        Return a list of actvities for a student
        """
        # Get the 'user_name' query parameter from the request
        user_name = request.query_params.get('user_name')

        # Get the current time
        current_time = timezone.now()

        activity_data = Activity.objects.filter(date_time_to_organize__gt=current_time).annotate(
            enroll_count=Count('student_activity_enrollment', filter=Q(student_activity_enrollment__status='enroll')),
            unenroll_count=Count('student_activity_enrollment', filter=Q(student_activity_enrollment__status='unenroll'))
        )

        # Data to be sent to the front-end
        sent_data = []

        for activity in activity_data:
            temp_act = {}
            
            temp_act['act_id'] = activity.id
            temp_act['activity_name'] = activity.activity_name
            temp_act['num_of_spots'] = activity.num_of_spots - (activity.enroll_count - activity.unenroll_count)

            if temp_act['num_of_spots'] == 0:
                temp_act['can_enroll'] = False
            else:
                temp_act['can_enroll'] = True

            # Check if the student has >= 3 no-show records. If he/she does, can_enroll = False
            one_year_ago = datetime.now() - timedelta(days=365)
            no_show_records = No_Show_Records.objects.filter(student__user_name=user_name, 
                                                             date_time_records__gt=one_year_ago)

            if no_show_records.count() >= 3:
                temp_act['can_enroll'] = False

            # If the student can enroll, check if the student has enrolled or not in the activities
            if temp_act['can_enroll']:
                stud_act_en = Student_Activity_Enrollment.objects.filter(student__user_name=user_name, 
                                                           activity__id=activity.id).last()
                
                if stud_act_en:
                    temp_act['is_enrolled'] = True if stud_act_en.status == "enroll" else False
                else:
                    temp_act['is_enrolled'] = False

            sent_data.append(temp_act)
                    
        return Response(sent_data)
    

class Enroll_Unenroll_View(APIView):
    def post(self, request):
        request_data = request.data
        user_name = request_data.get('user_name', None)
        student_status = request_data.get('status', None)
        activity_id = request_data.get('activity_id', None)

        if user_name is None or activity_id is None or student_status is None:
            return Response({'error': 'Missing or invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Use database transaction
            activity = Activity.objects.get(id=activity_id)
            student = Student.objects.filter(user_name=user_name).last()
            new_record = Student_Activity_Enrollment(student=student, activity=activity, status=student_status)
            new_record.save()

            # Return a success response with additional data if needed
            response_data = {
                'message': 'Enrollment/unenrollment successful',
                'enrollment_record_id': new_record.id,  # You can return the ID of the new record
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Activity.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)

        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions (e.g., database errors) here
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)