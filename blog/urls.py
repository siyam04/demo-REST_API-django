from django.urls import path
from blog.views import PostList, FilterPost, CreatePost

urlpatterns = [

    path('list/', PostList.as_view()),
    path('filter/', FilterPost.as_view()),
    path('create/', CreatePost.as_view()),
    path('detail/<int:id>', PostList.as_view()),

]