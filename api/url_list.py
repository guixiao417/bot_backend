from django.urls import path, include

urlpatterns = [
    path('bid', include('api.urls.bid')),  
    path('job', include('api.urls.job')),
    path('check-job', include('api.urls.check_job')),
    path('message', include('api.urls.message')),
]
