import requests
API_KEY = 'YOUR_YOUTUBE_API_KEY'
video_id = 'Ks-_Mh1QhMc'
url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={API_KEY}&part=snippet,contentDetails,statistics'
response = requests.get(url)
data = response.json()
if 'items' in data and len(data['items']) > 0:
    video_info = data['items'][0]
    title = video_info['snippet']['title']
    views = video_info['statistics']['viewCount']
    print(f'Назва відео: {title}')
    print(f'Перегляди: {views}')
else:
    print('Помилка отримання інформації про відео')