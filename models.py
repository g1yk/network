from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model




class User(AbstractUser):
    pass

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authors"
    )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name="liking", default=None, null=True, blank=True)
 
    class Meta:
        ordering = ['-date_created',]

    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args,**kwargs)
        if created:
            Like.objects.create(post=self)

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


# class Like(models.Model):
#     liked_by = models.ManyToManyField(User, related_name="likes", default=None, null=True, blank=True)
#     post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)

#     def __str__(self):
#         return "%s" % (self.post)





