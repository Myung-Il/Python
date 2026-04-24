import requests

username = input("본인의_깃허브_아이디를_입력하세요 : ")
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for key, value in data.items():
        print(f"{key}: {value}")
        
else:
    print(f"에러 발생: {response.status_code}")