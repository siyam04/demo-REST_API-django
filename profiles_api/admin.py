from django.contrib import admin
# Same App importing
from profiles_api.models import UserProfile, ProfileFeedItem


class UserProfileAdmin(admin.ModelAdmin):
    """ Customizing Fields for UserProfile Class """
    list_display = ['id', 'name', 'email', 'is_active', 'is_staff']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


class ProfileFeedItemAdmin(admin.ModelAdmin):
    """ Customizing Fields for UserProfile Class """
    list_display = ['id', 'user_profile', 'status_text', 'created_on']
    list_display_links = ['user_profile']
    list_filter = ['created_on', 'status_text']
    search_fields = ['status_text']


# Registering All Classes
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)

