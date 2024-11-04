from django.urls import path
from .views import CreateRetrievePosts, CreateRetrieveComment

urlpatterns = [
    path("create/post/", CreateRetrievePosts.as_view()),
    path("create/comment/", CreateRetrieveComment.as_view()),
]
