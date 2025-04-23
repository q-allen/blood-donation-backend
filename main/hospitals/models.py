from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.TextField()
    image = models.ImageField(upload_to='hospital_images/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name