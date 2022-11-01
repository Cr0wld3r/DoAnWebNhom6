from django.db import models

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title