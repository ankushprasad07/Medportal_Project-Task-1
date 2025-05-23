from django.db import models
from accounts.models import CustomUser

class BlogCategory(models.TextChoices):
    MENTAL_HEALTH = 'Mental Health'
    HEART_DISEASE = 'Heart Disease'
    COVID19 = 'Covid19'
    IMMUNIZATION = 'Immunization'

class BlogPost(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'})
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=50, choices=BlogCategory.choices)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
