from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer, DateRangeSerializer, AddPostSerializer


class PostList(APIView):

    def get(self, request, id=None):

        post_list = Post.objects.all()  # all()
        # post_list = Post.objects.filter()  # filter()
        # post_detail = Post.objects.get(id=id)  # get()
        post_ser = PostSerializer(post_list, many=True) # all(), filter()
        # post_ser = PostSerializer(post_detail)  # get()

        return Response(post_ser.data)


class FilterPost(APIView):

    def post(self, request):

        serializer = DateRangeSerializer(data=request.data)  # data= Used for data validation

        if serializer.is_valid():
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            posts = Post.objects.post_by_range(start_date, end_date)
            ser_data = PostSerializer(posts, many=True)
            msg = {'data': ser_data.data}

            return Response(msg, status=status.HTTP_200_OK)

        msg = {'status': serializer.errors}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class CreatePost(APIView):
    """Creating Post"""

    def post(self, request):
        serializer = AddPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            msg = {'data': True}
            return Response(msg, status=status.HTTP_200_OK)

        msg = {'status': serializer.errors}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
