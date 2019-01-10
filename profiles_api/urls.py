from django.urls import path
# Same App importing
# from profiles_api.views import HelloApiView
from profiles_api.views import HelloApiView

urlpatterns = [

    path('hello-view', HelloApiView.as_view(), name='hello-view'),

    # path('all-users', all_users, name='all-users'),
]

