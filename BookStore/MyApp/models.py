
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)  # Lưu link ảnh
    rating = models.FloatField()

    def __str__(self):
        return self.title
