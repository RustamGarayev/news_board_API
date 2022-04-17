from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from api.serializers import NewsPostSerializer, CommentSerializer
from core.models import NewsPost, Comment


class ListNewsPostAPIView(ListAPIView):
    """
    This endpoint list all the available todos from the database
    """
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


class CreateNewsPostAPIView(CreateAPIView):
    """
    This endpoint allows for creation of news post
    """
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


class UpdateNewsPostAPIView(UpdateAPIView):
    """
    This endpoint allows for updating specific news post by passing in the id of the news post to update
    """
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "News Post updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class DeleteNewsPostAPIView(DestroyAPIView):
    """
    This endpoint allows for deletion of a specific news post from the database
    """
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


class ListCommentAPIView(ListAPIView):
    """
    This endpoint list all the available todos from the database
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CreateCommentAPIView(CreateAPIView):
    """
    This endpoint allows for creation of comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpdateCommentAPIView(UpdateAPIView):
    """
    This endpoint allows for updating specific news post by passing in the id of the comment to update
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Comment updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class DeleteCommentAPIView(DestroyAPIView):
    """
    This endpoint allows for deletion of a specific comment from the database
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UpvotePostAPIView(APIView):
    """
    This endpoint allows to upvote specific news post
    """

    @staticmethod
    def post(request, pk):
        try:
            news_post = NewsPost.objects.get(pk=pk)
            news_post.upvote_post()

            return Response({"message": f"{news_post.title=} upvoted successfully"}, status=status.HTTP_201_CREATED)
        except NewsPost.DoesNotExist:
            return Response({"message": f"News post with this {pk=} does not exist"}, status=status.HTTP_404_NOT_FOUND)
