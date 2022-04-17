from django.db import models


class Post(models.Model):
    
    post = models.CharField(
        'post',
        max_length=300
    )
    # comments = models.ManyToManyField('Comment', related_name='postt')    
    def __str__(self) -> str:
        return f'{self.pk}: {self.post}'
    
    class Meta:
        verbose_name = 'Post'

    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comment') 
    parent = models.ManyToManyField('Comment', null=True, blank=True, related_name='children')
    
    text = models.CharField(
        'comment',
        max_length=300
    )

    def __str__(self) -> str:
        return f'{self.pk}: {self.text}'
    
    class Meta:
        verbose_name = 'Comment'

