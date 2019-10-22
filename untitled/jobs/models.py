from django.db import models

# Create your models here.

class Job(models.Model):
    """DB Model for Jobs"""
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    summary = models.TextField()

    def __str__(self):
        return self.title

