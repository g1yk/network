from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authors"
    )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created',]

    def __str__(self):
        return "%s" % (self.content)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    posts = models.ManyToManyField(Post)
    followers = models.ManyToManyField(User, related_name="follower")

    def __str__(self):
        return "%s" % (self.user)

class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following",  on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE,  default=None)
    def __str__(self):
        return "%s" % (self.user_id)

    class Meta:
        unique_together = ('user_id', 'following_user_id',)

class Follower(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return "%s" % (self.user)




