from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from gpost_app.models import Post
from gpost_app.serializers import PostSerializer

# Create your views here.
def index_view(request):
    return render(request, "index.html", {"headline": "Hello World!"})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_date')
    serializer_class = PostSerializer

    @action(detail=True, methods=['get', 'post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_field += 1
        post.save()
        return Response({'status': 'upvoted'})

    @action(detail=True, methods=['get', 'post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_field += 1
        post.save()
        return Response({'status': 'downvoted'})

    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(boast_roast='B').order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(boast_roast='R').order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def popular(self, request):
        most_popular = Post.objects.all().order_by('-votes')
        serializer = self.get_serializer(most_popular, many=True)
        return Response(serializer.data)