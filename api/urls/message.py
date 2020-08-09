from django.urls import path, include, re_path
from api.endpoint.message import MessageView

urlpatterns = [
    re_path(r'get', MessageView.as_view()),
    re_path(r'add', MessageView.as_view()),
]

