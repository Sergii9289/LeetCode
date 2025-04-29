import os
from google.cloud import vision
import io

# Встановлення шляху до облікових даних
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "valiant-airlock-458117-r6-439bafd2358c.json"

# Ініціалізація клієнта
client = vision.ImageAnnotatorClient()

# Завантаження зображення
file_name = 'input_image.jpg'
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Виявлення об'єктів
response = client.object_localization(image=image)
objects = response.localized_object_annotations

# Вивід виявлених об'єктів
for object_ in objects:
    print(f'Object name: {object_.name}')
    print(f'Score: {object_.score}')