from django.db import models
from django.utils import timezone

# Create your models here.

#The first model we will create is a post model

class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()

    def __unicode__(self):
        return self.title
