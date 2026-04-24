import matplotlib.pyplot as plt
import platform

# 한글 폰트 설정 (Windows: 맑은 고딕, Mac: AppleGothic)
if platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 800Hz 데이터
data_800 = {
    1 : {"Λ":0.426},
    2 : {"Λ":0.429},
    3 : {"Λ":0.428},
    4 : {"Λ":0.428},
    5 : {"Λ":0.426}
}

# 650Hz 데이터
data_650 = {
    1 : {"Λ":0.524},
    2 : {"Λ":0.522},
    3 : {"Λ":0.5213},
    4 : {"Λ":0.5233},
    5 : {"Λ":0.518}
}

# X축, Y축 데이터 추출
x_values = list(data_800.keys())
y_800 = [item["Λ"] for item in data_800.values()]
y_650 = [item["Λ"] for item in data_650.values()]

# 그래프 크기 설정
plt.figure(figsize=(10, 6))

# 800Hz 꺾은선 그래프 (파란색, 동그라미 마커)
plt.plot(x_values, y_800, marker='o', linestyle='-', color='blue', 
         markersize=8, linewidth=2, label='800Hz')

# 650Hz 꺾은선 그래프 (빨간색, 네모 마커)
plt.plot(x_values, y_650, marker='s', linestyle='-', color='crimson', 
         markersize=8, linewidth=2, label='650Hz')

# 그래프 제목, X/Y축 라벨 설정
plt.title('진동수에 따른 공명정상파의 파장 비교', fontsize=16, pad=15)
plt.xlabel('회차(회)', fontsize=12)
plt.ylabel('공명정상파의 파장(m)', fontsize=12)
plt.xticks(x_values)

# 800Hz 수치 표시 (선과 안 겹치게 파란색으로 표시)
for x, y in zip(x_values, y_800):
    ann = plt.annotate(
        str(y), 
        (x, y), 
        textcoords="offset points", 
        xytext=(0, 12), 
        ha='center', 
        fontsize=11, 
        fontweight='bold',
        color='darkblue'
    )
    ann.draggable(True) # ★ 마우스 드래그 기능 추가

# 650Hz 수치 표시 (선과 안 겹치게 빨간색으로 표시)
for x, y in zip(x_values, y_650):
    ann = plt.annotate(
        str(y), 
        (x, y), 
        textcoords="offset points", 
        xytext=(0, 12), 
        ha='center', 
        fontsize=11, 
        fontweight='bold',
        color='darkred'
    )
    ann.draggable(True) # ★ 마우스 드래그 기능 추가

# 범례(Legend) 추가 및 그리드 설정
plt.legend(fontsize=12, loc='best') # 그래프를 가리지 않는 최적의 위치에 범례 생성
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# 그래프 출력
plt.show()