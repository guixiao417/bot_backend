
import datetime
import random
from random import randrange
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Job, Category, Template, Bid
from authentication.models import User


class BidView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        request_data = request.data
        username = request_data['accountId']
        user = User.objects.filter(username=username).first()
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        title = request_data['title']
        description = request_data['description']
        skills = request_data['skills']
        project_id = request_data['projectId']
        job = Job.objects.filter(projectId=project_id).first()
        if job is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'No Job'})

        categories = self.get_ranked_categories(title, description, skills)
        if not len(categories):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'No Category'})

        template = self.get_template(user, categories[0]['category'])
        if not template:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'No Template'})
        Bid.objects.create(
            user=user,
            template=template,
            category=categories[0]['category'],
            rate=categories[0]['rate'],
            job=job
        )
        response = {"bid": template.template}
        job.bidder.add(user.id)
        job.save()
        return Response(response)

    def get_ranked_categories(self, title, description, skills):
        categories = Category.objects.all()
        category_list = []
        for category in categories:
            count = 0
            tags = category.tags.all()
            for tag in tags:
                tag_name = tag.name
                count = count + title.lower().count(tag_name)
                count = count + description.lower().count(tag_name)
                count = count + skills.lower().count(tag_name)
            if count:
                category_list.append(
                    {
                        'category': category,
                        'rate': round(count / len(tags), 2)
                    }
                )
        category_list.sort(key=lambda x: x['rate'], reverse=True)
        return category_list

    def get_template(self, user, category):
        templates = Template.objects.filter(user=user, category=category).all()
        if not len(templates):
            return False

        index = randrange(len(templates))
        selected_template = templates[index]
        return selected_template
