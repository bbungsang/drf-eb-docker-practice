from django.contrib.auth import get_user_model
from django.db import models

from config import settings

User = get_user_model()


class Post(models.Model):
    LEVEL = (
        ('H', 'HIGH'),
        ('M', 'MIDDLE'),
        ('L', 'LOW'),
    )
    level = models.CharField(choices=LEVEL, max_length=4)

    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    my_comment = models.OneToOneField(
        'Comment',
        blank=True,
        null=True,
        related_name='+',
    )

    def __str__(self):
        return '{}'.format(
            self.title,
        )


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.CharField(max_length=100)
