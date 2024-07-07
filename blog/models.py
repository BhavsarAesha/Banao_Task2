from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('mental_health', 'Mental Health'),
        ('heart_disease', 'Heart Disease'),
        ('covid19', 'Covid-19'),
        ('immunization', 'Immunization'),
    ]

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', default='default.jpg', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
