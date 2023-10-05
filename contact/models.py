from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(null=False, max_length=255)
    message = models.TextField()
    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["-email"]

