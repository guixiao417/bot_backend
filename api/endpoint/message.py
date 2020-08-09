import datetime
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import NewMessage, Account

class MessageView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        messages = NewMessage.objects.filter(checked=False, account__notification=True).all()
        for message in messages:
            message.checked = True
            message.save()

        if len(messages) == 0:
            return Response({"message": False})
        else:
            return Response({"message": True})


    def post(self, request, format=None):
        request_data = request.data
        accountId = request_data['accountId']
        account = Account.objects.filter(id=accountId).first()
        if account is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        created_at = datetime.datetime.now()
        NewMessage.objects.create(
            account=account,
            created_at=created_at,
            checked=False
        )
        return Response()