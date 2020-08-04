from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=120)
    task_deadline = models.DateTimeField()
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.task_text
