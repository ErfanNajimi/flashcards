from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flashcard(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=60)
    front = models.TextField()
    back = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-added_on"]
    
    def __str__(self):
        return f"{self.front}"
