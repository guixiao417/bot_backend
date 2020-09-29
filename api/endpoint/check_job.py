
import datetime
import nltk
from datetime import timedelta
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from api.models import Job, Account, Country
from api.serializers import JobSerializer, JobForBidSerializer
from ctrl.string_filter import check_title


class GetJobView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        jobs = Job.objects.filter(created_at__lte=datetime.datetime.now() - timedelta(days=8), check_status=False).all()
        serializer = JobForBidSerializer(jobs, many=True)
        return Response(serializer.data)


class CheckJobView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        request_data = request.data
        router = request_data['router']
        router1 = router + "/detail"
        router2 = router + ".html"
        job_status = request_data['status']
        job = Job.objects.filter(router=router).first()
        job1 = Job.objects.filter(router=router1).first()
        job2 = Job.objects.filter(router=router2).first()
        if job is not None:
            job.status = job_status
            job.check_status = True
            job.save()
            return Response()
        if job1 is not None:
            job1.status = job_status
            job1.check_status = True
            job1.save()
            return Response()
        if job2 is not None:
            job2.status = job_status
            job2.check_status = True
            job2.save()
            return Response()
        return Response(status=status.HTTP_400_BAD_REQUEST)
