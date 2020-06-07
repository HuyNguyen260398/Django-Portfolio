from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
