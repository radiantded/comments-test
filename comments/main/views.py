from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer
from django.db.models.query import Prefetch


class PostsView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    # def perform_create(self, serializer):
    #     serializer.save(post_id = self.kwargs.get('post_id'))
    def perform_create(self, serializer):
        # Post.objects.get(pk=self.kwargs.get('post_id')).comments.create(
        #     text=serializer.validated_data.get('text'),
        #     post_id=self.kwargs.get('post_id'))
        print(self.kwargs)
        if self.kwargs.get('pk'):
            Comment.objects.get(pk=self.kwargs.get('pk')).children.create(
                text=serializer.validated_data.get('text'),
                post_id=self.kwargs.get('post_id')
        )
        serializer.save(post_id=self.kwargs.get('post_id'))
        
    def get_queryset(self):
        """Возвращает комментарии поста в иерархическом виде"""
        # for c in Comment.objects.select_related('post').prefetch_related('children'):
        #     for b in c.__dict__['_prefetched_objects_cache']['children']:
        #         print(b.__dict__)
        return Comment.objects.select_related('post').prefetch_related('children')
        # return Comment.objects.filter(post_id=self.kwargs.get('post_id'))
        # return Pidoras.objects.filter(post_id=self.kwargs.get('post_id')).values()
    
    @action(['get', 'post'],
            detail=True)
    def related(self, *args, **kwargs):
        """Возвращает связанные комментарии и\или создаёт новый"""
        
        if self.request.method == 'POST':
            self.create(self.request)
        related_comments = Comment.objects.filter(parent=kwargs['pk']).values()
        return Response(related_comments)
