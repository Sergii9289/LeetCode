import requests
repo_owner = 'octocat'
repo_name = 'Hello-World'
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    print(f"Репозиторій: {data['name']}")
    print(f"Опис: {data['description']}")
    print(f"Зірки: {data['stargazers_count']}")
else:
    print('Помилка отримання інформації про репозиторій')