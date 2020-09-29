
import datetime
import random
from random import randrange
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Job, Category, Template, Url, Filter, Bid, Tag
from authentication.models import User


class BidView(APIView):
    permission_classes = [permissions.AllowAny]
    username = None
    title = None
    description = None
    skills = None
    account = None

    def post(self, request, format=None):
        request_data = request.data
        self.username = request_data['accountId']
        user = User.objects.filter(username=self.username).first()
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.title = request_data['title']
        self.description = request_data['description']
        self.skills = request_data['skills']
        _filter = user.filter.get()
        if not _filter:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        tags = self.get_ranked_tags()
        template = self.get_template()
        urls = self.get_urls(tags)
        bid = self.create_bid(template, urls)
        response = {"bid": bid, "id": template.id}
        return Response(response)

    def create_bid(self, template, urls):
        template_text = template.template
        url_text = ""
        for url in urls:
            url_text = url_text +  url.url + "\n"
        template_text = template_text.replace("@url@", url_text)
        template_text = template_text.replace("@account_name@", self.account.name)
        return template_text

    def get_ranked_tags(self):
        tags = Tag.objects.all()
        rank_list = []
        for tag in tags:
            tag_name = tag.name
            count = 0
            count = count + self.title.lower().count(tag_name)
            count = count + self.description.lower().count(tag_name)
            count = count + self.skills.lower().count(tag_name)
            if count:
                rank_list.append(
                    {
                        'tag': tag,
                        'count': count
                    }
                )
        rank_list.sort(key=lambda x: x['count'], reverse=True)
        return rank_list

    def get_template(self):
        templates = Template.objects.filter(account__id=self.accountId).all()
        index = randrange(len(templates)-1)
        selected_template = templates[index]
        return selected_template

    def get_urls(self, tags):
        query = None
        if tags == []:
            return []
        for i, tag in enumerate(tags):
            if i == 0:
                query = Url.objects.filter(tags=tag['tag'])
            else:
                query = query | Url.objects.filter(tags=tag['tag'])
        urls = query.all()
        urls = list(urls)
        if len(urls) > 5:
            urls = random.sample(urls, 5)
        return urls


class SaveBidView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        projectId = request.data['projectId']
        print(projectId)
        username = request.data['accountId']
        bot = request.data['bot']
        templateId = request.data['templateID']

        user = User.objects.filter(username=username).first()
        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        job = Job.objects.filter(projectId=projectId).first()
        if job is None:
            print("no job")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        template = Template.objects.filter(id=templateId).first()
        if template is None:
            print("no template")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        created_at = datetime.datetime.now()

        Bid.objects.create(
            job=job,
            user=user,
            template=template,
            bot=bot,
            created_at=created_at
        )
        return Response('success')
       