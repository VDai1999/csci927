from rest_framework import serializers
from .models import *


class Activity_Serializer(serializers.Serializer):
    act_id = serializers.IntegerField()
    activity_name = serializers.CharField(max_length=200)
    num_of_spots = serializers.IntegerField()
    is_enrolled =  serializers.BooleanField()
    can_enroll = serializers.BooleanField()