from django.db import models

# Create your models here.
class Tasks(models.Model):
    Task = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)     
    # Add other fields as needed

    def __str__(self):
        return self.task
    

class Todo(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=100)     
    # Add other fields as needed

    def __str__(self):
        return self.task
    
class DeletedTask(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=100)     
    # Add other fields as needed

    def __str__(self):
        return self.task
