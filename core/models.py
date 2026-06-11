from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    # Link the resume to a specific user (if user is deleted, delete their resumes)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Basic info
    title = models.CharField(max_length=100, default="Untitled Resume") # e.g. "Software Engineer"
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    
    # Large text fields
    summary = models.TextField(blank=True)
    skills = models.TextField(blank=True) # We will store comma-separated skills
    
    # Auto-update timestamp
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"