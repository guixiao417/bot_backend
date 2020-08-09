from django.urls import path, include, re_path
from api.endpoint.bid import BidView, SaveBidView

urlpatterns = [
    re_path(r'get', BidView.as_view()),
    re_path(r'save', SaveBidView.as_view())
]

