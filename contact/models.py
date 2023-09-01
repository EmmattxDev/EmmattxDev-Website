from django.db import models

# Create your models here.
# fName = request.POST["fName"]
#         email = request.POST["email"]
#         sbj = request.POST["sbj"]
#         msg = request.POST["msg"]

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

