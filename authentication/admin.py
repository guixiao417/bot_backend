from django.contrib import admin
from authentication.models import User, Address, UserRole, Location


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'email', 'first_name', 'last_name', 'username', 'country', 'city', 'last_login',
                    'is_active', 'avatar']


admin.site.register(User, UserAdmin)


class UserRoleAdmin(admin.ModelAdmin):
    model = UserRole
    list_display = ['id',  'user', 'role']


admin.site.register(UserRole, UserRoleAdmin)


class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ['id', 'user', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state',  'country',
                  'postal_code', 'phone', 'primary']


admin.site.register(Address, AddressAdmin)



class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['id', 'address1', 'address2', 'city', 'state', 'country']


admin.site.register(Location, LocationAdmin)
