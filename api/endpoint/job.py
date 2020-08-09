
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

class AddJobView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        request_data = request.data
        country_name = request_data['country']
        country = Country.objects.filter(name=country_name).first()
        if country is None:
            Country.objects.create(name=country_name)
        projectId = request_data['projectId']
        project = Job.objects.filter(projectId=projectId).first()
        if project is not None:
            project.count = project.count + 1
            
            project.save()
            return Response()
        memberDate = request_data['memberDate']
        request_data['memberDate'] = datetime.datetime.fromtimestamp(int(memberDate)/1000).isoformat()
        request_data['created_at'] = datetime.datetime.now()
        serializer = JobSerializer(data=request_data)
        if serializer.is_valid():
            try:
                serializer.save()
            except:
                request_data['title'] = 'unknown'
                serializer = JobSerializer(data=request_data)
                serializer.is_valid()
                serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetJobView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        request_data = request.data
        accountId = request_data['accountId']
        account = Account.objects.filter(id=accountId).first()
        if account is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        filtered_countries = []
        countries = account.countries.all()
        for country in countries:
            filtered_countries.append(country.name)
        query = Job.objects.filter(created_at__gte=datetime.datetime.now() - timedelta(minutes=account.time_delta)) \
        .filter(Q(maxBudget__gte=account.fixed_budget, hourly=False) | Q(maxBudget__gte=account.hourly_budget, hourly=True)) \
        .exclude(disabled=True).exclude(Q(bidder=account) | Q(bot=account)).exclude(country__in=filtered_countries)
        if account.payment_filter:
            query = query.filter(Q(v_payment=True) | Q(v_deposit=True))
        jobs = query.order_by('-created_at').all()
        keyworks = ['seo', 'ai', 'ar', 'ml', 'ux/ui', 'magento', 'wordpress', 'wix', 'tiktok', 'photoshop', 'shopify', 'drupal', 'game', 'design', 'wp', 'blog', 'india', 'odoo']
        job_list = []
        
        for job in jobs:
            text_split = nltk.word_tokenize(job.title)
            title_tokens = []
            for x in text_split:
                if x not in title_tokens:
                    title_tokens.append(x.lower())
            if check_title(keyworks, title_tokens):
                continue

            job.bot.add(account.id)
            job.save()
            job_list.append(job)
            
        jobs = job_list[:account.job_count]
        serializer = JobForBidSerializer(jobs, many=True)
        return Response(serializer.data)



class CheckJobView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        request_data = request.data
        router = request_data['router']
        accountId = request_data['accountId']
        account = Account.objects.filter(id=accountId).first()
        if account is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        job = Job.objects.filter(router=router).first()
        if job is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        job.checked = True
        job.bot.add(account.id)
        job.save()
        return Response()