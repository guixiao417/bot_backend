from django.urls import path, include, re_path
from api.endpoint.job import AddJobView, GetJobView, CheckJobView

urlpatterns = [
    re_path(r'add', AddJobView.as_view()),
    re_path(r'get', GetJobView.as_view()),
    re_path(r'check', CheckJobView.as_view())
]

