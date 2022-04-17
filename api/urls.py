from django.urls import path
from api import views

urlpatterns = [
    path("news-post/list/", views.ListNewsPostAPIView.as_view(), name="news_post_list"),
    path("news-post/create/", views.CreateNewsPostAPIView.as_view(), name="news_post_create"),
    path("news-post/update/<int:pk>/", views.UpdateNewsPostAPIView.as_view(), name="update_news_post"),
    path("news-post/delete/<int:pk>/", views.DeleteNewsPostAPIView.as_view(), name="delete_news_post"),
    path("comment/list/", views.ListCommentAPIView.as_view(), name="comment_list"),
    path("comment/create/", views.CreateCommentAPIView.as_view(), name="comment_create"),
    path("comment/update/<int:pk>/", views.UpdateCommentAPIView.as_view(), name="update_comment"),
    path("comment/delete/<int:pk>/", views.DeleteCommentAPIView.as_view(), name="delete_comment"),
    path("upvote-post/<int:pk>/", views.UpvotePostAPIView.as_view(), name="upvote_post"),
]
