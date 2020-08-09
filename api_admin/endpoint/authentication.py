from rest_framework_jwt.views import JSONWebTokenAPIView
from api_admin.serializers import JSONWebTokenSerializer


class ObtainJwtToken(JSONWebTokenAPIView):
    """
    Get jwt token
    @ params:  username, password, store
    """
    serializer_class = JSONWebTokenSerializer
