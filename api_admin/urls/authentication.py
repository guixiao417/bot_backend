from django.urls import path, include, re_path
from api_admin.endpoint import authentication

urlpatterns = [
    re_path(r'jwt', authentication.ObtainJwtToken.as_view())                  # get jwt token for admin, agent
]

