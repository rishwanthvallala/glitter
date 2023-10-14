from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    likers = models.ManyToManyField(User, related_name="likes", blank=True)
    likes= models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=  True)

    def __str__(self):
        return f'''{self.user} posted "{self.content}" '''
    
class follow_status(models.Model):
    is_verified = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    following = models.ManyToManyField(User, related_name="following", blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)

    
    def __str__(self):
        return f"{self.user} is following {self.following.count()} people and is followed by {self.followers.count()} people"