from django.db import models

# Create your models here.
class Project(models.Model):
    PROJECT_TYPES = [
        ('Website', 'Website'),
        ('Web App', 'Web Application'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    description = models.TextField()
    link = models.URLField()
    type = models.CharField(max_length=50, choices=PROJECT_TYPES, default='Website')  # Dropdown field

    def __str__(self):
        return self.title

class Documents(models.Model):
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name
