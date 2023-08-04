from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    author = models.CharField(max_length=20)  
    post = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.author

class Comment(models.Model):
    author = models.CharField(max_length=20)  
    comment = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default=1)  # ForeignKey linking Comment to Post
    

    def __str__(self):
        return self.author + "'s comment on " + self.post.author + "'s post"
