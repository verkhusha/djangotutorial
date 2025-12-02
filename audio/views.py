from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .sound_model import predict_sound
from .models import AudioFile

def index(request):
    result = None
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        file_path = fs.path(filename)

        result = predict_sound(file_path)

        # Зберігаємо в базу
        AudioFile.objects.create(
            file=filename,
            predicted_class=result['class'],
            category=result['category'],
            confidence=result['confidence']
        )

    return render(request, 'audio/index.html', {'result': result})
