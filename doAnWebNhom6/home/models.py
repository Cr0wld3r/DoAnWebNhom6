from django.db import models

# Create your models here.
class CompanyHomePageDisplay(models.Model):
    title = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title