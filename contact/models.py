from django.db import models
from django.utils import timezone


CAT_CHOICES = (('MR', 'Mr.'),('MRS', 'Mrs.'),('MS', 'Ms.'))

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=3, choices=CAT_CHOICES)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
