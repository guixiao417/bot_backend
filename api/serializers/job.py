from rest_framework import serializers
from api.models import Job
from random import randrange


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'title', 'hourly', 'currency', 'budget', 'maxBudget', 'recruiter', 'skills', 'country', 'completedJob', 'projectId', 'memberDate', 'v_identity', 'v_payment', 'v_deposit', 'v_email', 'v_profile', 'v_phone', 'router', 'created_at')


class JobForBidSerializer(serializers.ModelSerializer):
    interval_time = serializers.SerializerMethodField()   

    def get_interval_time(self, obj):
        interval_time = (randrange(10) + 20) * 1000
        return interval_time
    class Meta:
        model = Job
        fields = ('router', 'interval_time')
