from rest_framework import serializers

from .models import Post, Comment


class FilterCommentSerializer(serializers.ListSerializer):
    
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    
    def to_representation(self, instance):
        # print(self.context)
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        list_serializer_class = FilterCommentSerializer
        fields = ('id', 'text', 'children')
        # depth = 3
