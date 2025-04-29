import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Ваш API-ключ OpenAI
api_key = os.getenv('AI_TOKEN')

# Аутентифікація
openai.api_key = api_key

# Запит до моделі ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Використовуйте актуальну модель
    messages=[
        {"role": "system", "content": "Ти розумний помічник."},
        {"role": "user", "content": "Кількість населення Пакістану"}
    ]
)

# Друк відповіді
print(response['choices'][0]['message']['content'])