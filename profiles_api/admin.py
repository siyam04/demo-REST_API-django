from django.contrib import admin
# Same App importing
from profiles_api.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """ Customizing Fields for UserProfile Class """
    list_display = ['id', 'name', 'email', 'is_active', 'is_staff']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


# Registering All Classes
admin.site.register(UserProfile, UserProfileAdmin)
