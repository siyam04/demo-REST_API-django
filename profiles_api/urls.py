from django.urls import path

# API importing
from rest_framework.routers import DefaultRouter

# Same App importing
from profiles_api.views import (
    UserProfileViewSet,
    HelloApiView,
    HelloViewSet,
    LoginViewSet,
    UserProfileFeedViewSet,
)


# Router used for connecting Api ViewSet. It also need to register.
router = DefaultRouter()
# Router registering with CBVs.
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet) # No need base_name for ModelViewSet
router.register('login', LoginViewSet, base_name='login')
router.register('login', LoginViewSet, base_name='login')
router.register('feed', UserProfileFeedViewSet) # No need base_name for ModelViewSet


urlpatterns = [

    path('hello-api-view', HelloApiView.as_view(), name='hello-api-view'),

    # No need do define ViewSet URL in here.

]

