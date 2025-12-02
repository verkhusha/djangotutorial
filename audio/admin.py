from django.contrib import admin
from .models import AudioFile

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'predicted_class', 'category', 'confidence', 'uploaded_at')
