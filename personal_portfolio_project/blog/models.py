from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
