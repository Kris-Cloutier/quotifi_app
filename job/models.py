from django.db import models

# Create your models here.

class Job(models.Model):
    job_number = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    
