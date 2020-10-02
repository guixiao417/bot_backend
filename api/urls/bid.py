from django.urls import path, include, re_path
from api.endpoint.bid import BidView

urlpatterns = [
    re_path(r'get', BidView.as_view()),
]

