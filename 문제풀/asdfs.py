import matplotlib.pyplot as plt
import platform

# 한글 폰트 설정 (Windows: 맑은 고딕, Mac: AppleGothic)
if platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 800Hz
data_800 = {
    1 : {"(m/s)":340.80},
    2 : {"(m/s)":343.20},
    3 : {"(m/s)":342.40},
    4 : {"(m/s)":342.40},
    5 : {"(m/s)":340.80}
}
# 650Hz
data_650 = {
    1 : {"(m/s)":340.60},
    2 : {"(m/s)":339.30},
    3 : {"(m/s)":338.85},
    4 : {"(m/s)":340.15},
    5 : {"(m/s)":336.70}
}

# X축, Y축 데이터 추출
x_values = list(data_800.keys())
y_800 = [item["(m/s)"] for item in data_800.values()]
y_650 = [item["(m/s)"] for item in data_650.values()]

# 그래프 크기 설정
plt.figure(figsize=(10, 6))

# 800Hz 꺾은선 그래프 (파란색, 동그라미 마커)
plt.plot(x_values, y_800, marker='o', linestyle='-', color='blue', 
         markersize=8, linewidth=2, label='800Hz')

# 650Hz 꺾은선 그래프 (빨간색, 네모 마커)
plt.plot(x_values, y_650, marker='s', linestyle='-', color='crimson', 
         markersize=8, linewidth=2, label='650Hz')

# 그래프 제목, X/Y축 라벨 설정
plt.title('진동수에 따른 소리 속도의 실험값 비교', fontsize=16, pad=15)
plt.xlabel('회차(회)', fontsize=12)
plt.ylabel('소리 속도의 실험값(m/s)', fontsize=12)
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