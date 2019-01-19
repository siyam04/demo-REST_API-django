# Same App importing
from profiles_api.models import UserProfile

# API importing
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update his own status"""

        if request.method in SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id



