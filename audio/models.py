from django.db import models

class AudioFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    predicted_class = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.file.name
