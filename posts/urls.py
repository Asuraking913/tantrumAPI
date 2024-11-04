from django.urls import path
from .views import CreateRetrievePosts

urlpatterns = [path("create/post/", CreateRetrievePosts.as_view())]
