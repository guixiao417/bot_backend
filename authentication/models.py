from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class User(AbstractUser):

    first_name = models.CharField(max_length=400, null=True, blank=True)
    last_name = models.CharField(max_length=400, null=True, blank=True)
    country = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=400)
    username = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    avatar = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email

    @property
    def roles(self):
        roles = self.role.all()
        _roles = []
        for role in roles:
            _roles.append(role.role)
        return _roles


class Location(models.Model):
    address1 = models.CharField(max_length=800, blank=True, null=True)
    address2 = models.CharField(max_length=800, blank=True, null=True)
    city = models.CharField(max_length=800, blank=True, null=True)
    state = models.CharField(max_length=800, blank=True, null=True)
    country = models.CharField(max_length=800, blank=True, null=True)
    postal_code = models.CharField(max_length=800, blank=True, null=True)


class UserRole(models.Model):
    ROLE_ADMIN = 0
    ROLE_GROUP_OWNER = 1
    ROLE_EXPERT = 2
    ROLE_VERIFIED = 3

    ROLE_CHOICES = (
        (ROLE_ADMIN, "admin"),
        (ROLE_GROUP_OWNER, "group owner"),
        (ROLE_EXPERT, "expert"),
        (ROLE_VERIFIED, "verified"),
    )

    user = models.ForeignKey(User, to_field='id', related_name='role', on_delete=models.CASCADE)
    role = models.IntegerField(default=1, choices=ROLE_CHOICES)


class Address(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=800, blank=True, null=True)
    last_name = models.CharField(max_length=800, blank=True, null=True)
    address1 = models.CharField(max_length=800, blank=True, null=True)
    address2 = models.CharField(max_length=800, blank=True, null=True)
    city = models.CharField(max_length=800, blank=True, null=True)
    state = models.CharField(max_length=800, blank=True, null=True)
    country = models.CharField(max_length=800, blank=True, null=True)
    postal_code = models.CharField(max_length=800, blank=True, null=True)
    phone = models.CharField(max_length=800, blank=True, null=True)
    primary = models.BooleanField(default=False)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return str(self.pk)

