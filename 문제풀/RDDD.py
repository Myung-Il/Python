import random as r

random_n=r.randrange(1,101)
cnt=0
while 1:
    n=int(input('답을 입력해봅시다 : '))
    cnt+=1
    if n>random_n:
        print('아 이건 너무 큰데요')
    elif n<random_n:
        print('아 이건 좀 작은데')
    else:
        print('오 정답입니다')
        print(f'총 횟수 {cnt}만에')
        break


'''
정답과의 거리에 따라서
가까우면 가깝다
더 가까우면 매우 가깝다 처럼

수정하기
다음주 수요일에 평가
'''

'''
행맨 만들기
'''