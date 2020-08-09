from rest_framework import generics, permissions
from authentication.models import User, UserRole
from authentication.serializers import UserSerializer


class UserManagementView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects
        return queryset


class UserManagementDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = User.objects.filter(pk=user_id)
        return queryset


class UserManagementUpdateView(generics.DestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = User.objects.filter(pk=user_id)
        return queryset


class AdminManagementView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        roles = UserRole.objects.filter(role=UserRole.ROLE_ADMIN).all()
        admin_list = []
        for role in roles:
            admin_list.append(role.user.id)
        queryset = User.objects.filter(pk__in=admin_list)
        return queryset
