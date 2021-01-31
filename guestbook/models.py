from django.db import models

# Create your models here.
class Post(models.Model):
    writer = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name


class Comment(models.Model):
    content = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post",on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]
