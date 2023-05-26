from django.db import models

class ProjectPlatform(models.Model):
    project_name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    repository_link = models.URLField(max_length=100)
    
    def __str__(self):
        return self.project_name
    
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    Self_description = models.CharField(max_length=200)
    project = models.ForeignKey(ProjectPlatform, on_delete=models.CASCADE, related_name="userlist") 
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    