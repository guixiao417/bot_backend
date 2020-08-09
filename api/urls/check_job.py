from django.urls import path, include, re_path
from api.endpoint.check_job import  GetJobView, CheckJobView

urlpatterns = [
    re_path(r'get', GetJobView.as_view()),
    re_path(r'check', CheckJobView.as_view())
]

