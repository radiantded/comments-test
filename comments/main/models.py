from django.db import models


class Post(models.Model):

    post = models.CharField(
        'post',
        max_length=300
    )

    def __str__(self) -> str:
        return f'{self.pk}: {self.post}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comment'
    )
    parent = models.ManyToManyField(
        'Comment',
        blank=True,
        related_name='children'
    )
    text = models.CharField(
        'comment',
        max_length=300
    )

    def __str__(self) -> str:
        return f'{self.pk}: {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
