from django.urls import path, include, re_path
from api_admin.endpoint import user_management

urlpatterns = [
    re_path(r'customers', user_management.UserManagementView.as_view()),                  # post user
    re_path(r'(?P<pk>\d+)/update', user_management.UserManagementDeleteView.as_view()),   # update user
    re_path(r'(?P<pk>\d+)/delete', user_management.UserManagementUpdateView.as_view()),   # delete user
    re_path(r'admin', user_management.AdminManagementView.as_view()),                     # post user
]

