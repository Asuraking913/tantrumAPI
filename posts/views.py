from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer

# Create your views here.


def home_page(request):
    return render(request, "home.html")


class CreateRetrievePosts(generics.ListCreateAPIView):
    serializer_class = PostSerializer


class CreateRetrieveComment(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
