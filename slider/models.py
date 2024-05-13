from django.db import models
from filer.fields.image import FilerImageField

class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title