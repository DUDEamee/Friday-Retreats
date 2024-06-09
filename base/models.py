from django.db import models

# Create your models here.

class Data(models.Model):
    Title = models.CharField(max_length=100)
    Price = models.FloatField()
    Description = models.TextField()
    Image = models.ImageField(upload_to='images/')

    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title