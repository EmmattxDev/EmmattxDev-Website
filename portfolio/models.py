from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, null=False, primary_key=True, unique=True)
    slug = models.SlugField(default='', blank=True)
    about = models.TextField(blank=False)
    stack = models.CharField(max_length=200, null=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='', blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('portfolio:portfolio_details', args=[str(self.slug)])


class Experience(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    title = models.CharField(max_length=150, null=False, unique=True)
    company = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    started = models.DateField(null=False)
    ended = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-started']