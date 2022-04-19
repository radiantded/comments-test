from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostsView(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs.get('post_id'))


class CommentView(ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Создаёт корневой или дочерний комментарий"""

        comment_id = self.kwargs.get('pk')
        post_id = self.kwargs.get('post_id')
        if comment_id:
            get_object_or_404(Comment, pk=comment_id).children.create(
                text=serializer.validated_data.get('text'),
                post_id=post_id
            )
        else:
            serializer.save(post_id=post_id)

    def get_queryset(self):
        """Возвращает комментарии поста"""

        return Comment.objects.filter(
            post_id=self.kwargs.get('post_id')
        ).prefetch_related('children')

    @action(['get', 'post'], detail=True)
    def related(self, *args, **kwargs):
        """Возвращает дочерние комментарии и/или создаёт новый"""

        if self.request.method == 'POST':
            return self.create(self.request)
        return Response(
            list(get_object_or_404(
                Comment, pk=kwargs.get('pk')).children.values()))
