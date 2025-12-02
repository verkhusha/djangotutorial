import tensorflow as tf
import tensorflow_hub as hub
import librosa
import numpy as np
import urllib.request

model = hub.load('https://tfhub.dev/google/yamnet/1')

url = 'https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv'
class_map_path, _ = urllib.request.urlretrieve(url)
class_names = [line.strip().split(',')[2] for line in open(class_map_path).read().splitlines()[1:]]

CATEGORY_MAP = {
    "Людські звуки": [
        "Speech", "Whispering", "Laughter", "Crying", "Singing", "Cough", "Sneeze", "Breathing", "Snoring"
    ],
    "Тварини": [
        "Dog", "Bark", "Cat", "Meow", "Bird", "Chirp", "Frog", "Insect", "Roar", "Moo", "Neigh"
    ],
    "Музика": [
        "Music", "Guitar", "Piano", "Violin", "Drum", "Flute", "Saxophone", "Trumpet", "Singing"
    ],
    "Природа": [
        "Rain", "Thunder", "Wind", "Fire", "Water", "Wave", "Crackling"
    ],
    "Транспорт": [
        "Car", "Motorcycle", "Vehicle", "Airplane", "Train", "Boat", "Bus", "Subway", "Engine", "Siren", "Horn"
    ],
    "Побут / техніка": [
        "Door", "Footsteps", "Typing", "Vacuum", "Blender", "Microwave", "Clock", "Toilet", "TV", "Telephone"
    ],
    "Сигнали / шуми": [
        "Alarm", "Explosion", "Gunshot", "Glass", "Buzzer", "Beep", "Noise", "Silence", "Applause"
    ]
}


def get_category(class_name: str) -> str:
    for category, keywords in CATEGORY_MAP.items():
        for key in keywords:
            if key.lower() in class_name.lower():
                return category
    return "Інше"


def predict_sound(file_path: str) -> dict:
    wav, sr = librosa.load(file_path, sr=16000)

    if len(wav.shape) > 1:
        wav = np.mean(wav, axis=1)

    wav_tensor = tf.convert_to_tensor(wav, dtype=tf.float32)

    scores, embeddings, spectrogram = model(wav_tensor)
    mean_scores = tf.reduce_mean(scores, axis=0)
    class_index = int(np.argmax(mean_scores))
    class_name = class_names[class_index]
    confidence = float(mean_scores[class_index]) * 100

    category = get_category(class_name)

    result = {
        "class": class_name,
        "category": category,
        "confidence": round(confidence, 2)
    }

    print(f"Розпізнано: {result['class']}  "
          f"(категорія: {result['category']}, "
          f"ймовірність: {result['confidence']}%)")

    return result
