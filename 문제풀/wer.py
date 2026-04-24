import requests
from collections import Counter

# 1. 대상 닉네임 설정
# username = "myung-il" # 예시: 리눅스 창시자 리누스 토발즈
username = "geonhwi82"
url = f"https://api.github.com/users/{username}/repos"

# 2. 레포지토리 목록 가져오기 (직행)
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    
    # 3. language 데이터만 수집하기
    used_languages = []
    for repo in repos:
        lang = repo.get('language')
        if lang is not None: # 언어가 지정되지 않은 빈 레포지토리 제외
            used_languages.append(lang)
            
    # 4. 통계 내기 (어떤 언어를 몇 번 주력으로 썼는지)
    language_stats = Counter(used_languages)
    
    print(f"[{username}님의 주력 언어 통계]")
    for lang, count in language_stats.most_common():
        print(f"- {lang}: {count}개 프로젝트")
        
else:
    print("데이터를 가져오는데 실패했습니다.")